import logging
import os.path
import ssl
import time
from typing import Union
from urllib.parse import urlencode
from importlib.util import find_spec

import requests
from requests import Session
from requests.adapters import HTTPAdapter

import rosreestr_api


logger = logging.getLogger(__name__)


class BaseHTTPClient:
    SESSION_CLS = Session

    GET_HTTP_METHOD = 'GET'
    POST_HTTP_METHOD = 'POST'
    PATCH_HTTP_METHOD = 'PATCH'
    PUT_HTTP_METHOD = 'PUT'

    BODY_LESS_METHODS = [GET_HTTP_METHOD]
    LOG_REQUEST_TEMPLATE = '%(method)s %(url)s%(request_body)s%(duration)s'
    LOG_RESPONSE_TEMPLATE = (LOG_REQUEST_TEMPLATE +
                             ' - HTTP %(status_code)s%(response_body)s%(duration)s')

    def __init__(self, timeout=3, keep_alive=False, default_headers=None):
        self.timeout = timeout
        self.keep_alive = keep_alive
        self.default_headers = default_headers or {}
        self._session = None

    @property
    def session(self) -> requests.Session:
        if self.keep_alive:
            if not self._session:
                self._session = self.SESSION_CLS()
            return self._session
        else:
            return self.SESSION_CLS()

    def get(self, url, params=None, **kwargs) -> requests.Response:
        if params:
            url_with_query_params = url + '?' + urlencode(params)
        else:
            url_with_query_params = url

        return self._make_request(self.GET_HTTP_METHOD, url_with_query_params, **kwargs)

    def post(self, url, **kwargs) -> requests.Response:
        return self._make_request(self.POST_HTTP_METHOD, url, **kwargs)

    def patch(self, url, **kwargs) -> requests.Response:
        return self._make_request(self.PATCH_HTTP_METHOD, url, **kwargs)

    def put(self, url, **kwargs) -> requests.Response:
        return self._make_request(self.PUT_HTTP_METHOD, url, **kwargs)

    def _log_request(self, method, url, body, duration=None, log_method=logger.info):
        message_params = {
            'method': method, 'url': url, 'request_body': _get_body_for_logging(body),
            'duration': _get_duration_for_logging(duration)}
        log_method(self.LOG_REQUEST_TEMPLATE, message_params)

    def _log_response(self, response, duration, log_method=logger.info):
        message_params = {
            'method': response.request.method,
            'url': response.request.url,
            'request_body': _get_body_for_logging(response.request.body),
            'status_code': response.status_code,
            'response_body': _get_body_for_logging(response.content),
            'duration': _get_duration_for_logging(duration)}
        log_method(self.LOG_RESPONSE_TEMPLATE, message_params)

    def _make_request(self, method, url, **kwargs) -> requests.Response:
        kwargs.setdefault('timeout', self.timeout)
        session = self.session
        timeout = kwargs.pop('timeout', self.timeout)

        headers = self.default_headers.copy()
        headers.update(kwargs.pop('headers', {}))

        request = requests.Request(method, url, headers=headers, **kwargs)
        prepared_request = request.prepare()
        self._log_request(method, url, prepared_request.body)
        start_time = time.time()
        try:
            response = session.send(prepared_request, timeout=timeout)
            duration = time.time() - start_time
            if response.status_code >= 400:
                log_method = logging.error
            else:
                log_method = logging.debug

            self._log_response(response, duration=duration, log_method=log_method)
            return response
        except requests.exceptions.RequestException as e:
            duration = time.time() - start_time
            if e.response:
                self._log_response(e.response, duration=duration, log_method=logging.error)
            else:
                self._log_request(method, url, prepared_request.body, log_method=logging.exception)
            raise
        finally:
            if not self.keep_alive:
                session.close()


class HTTPSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ssl_context = ssl.create_default_context()
        # https://www.openssl.org/docs/man3.0/man3/SSL_CTX_set_security_level.html
        # rosreestr supports only SECLEVEL 1
        ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')
        # We want to use the most secured protocol from security level 1
        ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2
        kwargs['ssl_context'] = ssl_context
        return super().init_poolmanager(*args, **kwargs)


class CustomSession(Session):
    CACERT_PATH = os.path.join(
        os.path.dirname(find_spec(rosreestr_api.__name__).origin),
        'cacert.pem'
    )
    def __init__(self):
        super().__init__()
        self.verify = self.CACERT_PATH
        self.mount(prefix='https://', adapter=HTTPSAdapter())


class RosreestrHTTPClient(BaseHTTPClient):
    SESSION_CLS = CustomSession


def _get_body_for_logging(body: Union[bytes, str]) -> str:
    try:
        if isinstance(body, bytes):
            return (b' BODY: ' + body).decode('utf-8')
        elif isinstance(body, str):
            return ' BODY: ' + body
        else:
            return ''
    except UnicodeDecodeError:
        return ''


def _get_duration_for_logging(duration: str) -> str:
    if duration is not None:
        return ' {0:.6f}s'.format(duration)
    else:
        return ''
