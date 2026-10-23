import json

import pytest
import httpretty
import requests

from tests import nspd_client_fixtures, rosreestr_client_fixtures
from rosreestr_api.clients.rosreestr import (
    RosreestrAPIClient,
    NSPDAPIClient,
)


class TestRosreestrAPIClient:

    SEARCH_OBJECTS_BY_ADDRESS_URL = 'https://lk.rosreestr.ru/account-back/address/search'

    CONTENT_TYPE_JSON = 'application/json'

    @httpretty.activate
    def test_get_objects_by_address(self):
        address = 'Москва, ул Красного Маяка, д 22, к 2, кв 187'
        httpretty.register_uri(
            method=httpretty.GET, uri=self.SEARCH_OBJECTS_BY_ADDRESS_URL,
            body=rosreestr_client_fixtures.OBJECTS_BY_ADDRESS_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()
        objects = api_client.get_objects_by_address(address)

        assert rosreestr_client_fixtures.OBJECTS_BY_ADDRESS == objects
        assert {'term': [address]} == httpretty.last_request().querystring

    @httpretty.activate
    def test_get_objects_by_address_not_found(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.SEARCH_OBJECTS_BY_ADDRESS_URL, body=b'[]',
            content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()

        assert [] == api_client.get_objects_by_address('Казань, Ибрагимова 53б, кв 1')


class TestNSPDAPIClient:

    NSPD_SEARCH_URL = 'https://nspd.gov.ru/api/geoportal/v2/search/geoportal'
    NSPD_PARCELS_WMS_URL = 'https://nspd.gov.ru/api/aeggis/v3/36048/wms'
    NSPD_BUILDINGS_WMS_URL = 'https://nspd.gov.ru/api/aeggis/v3/36049/wms'
    NSPD_REFERER = 'https://nspd.gov.ru/map?thematic=PKK'

    CONTENT_TYPE_JSON = 'application/json'

    @httpretty.activate
    def test_get_parcel_by_coordinates(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_PARCELS_WMS_URL,
            body=nspd_client_fixtures.PARCEL_BY_COORDINATES_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = NSPDAPIClient()
        obj = api_client.get_parcel_by_coordinates(lat=55.761, long=37.6096, limit=5)

        assert nspd_client_fixtures.PARCEL_BY_COORDINATES == obj
        request = httpretty.last_request()
        query = {key: value[0] for key, value in request.querystring.items()}
        assert 'GetFeatureInfo' == query['REQUEST']
        assert '36048' == query['LAYERS'] == query['QUERY_LAYERS']
        assert 'EPSG:3857' == query['CRS']
        assert 'application/json' == query['INFO_FORMAT']
        assert '5' == query['FEATURE_COUNT']
        min_x, min_y, max_x, max_y = map(float, query['BBOX'].split(','))
        # the point in EPSG:3857
        assert (min_x + max_x) / 2 == pytest.approx(4186681.52, abs=0.01)
        assert (min_y + max_y) / 2 == pytest.approx(7510983.89, abs=0.01)
        assert self.NSPD_REFERER == request.headers['Referer']

    @httpretty.activate
    def test_get_parcel_by_cadastral_id(self):
        cadastral_id = '72:17:1502001:499'
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_SEARCH_URL,
            body=nspd_client_fixtures.PARCEL_BY_CADASTRAL_ID_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = NSPDAPIClient()
        obj = api_client.get_parcel_by_cadastral_id(cadastral_id)

        assert nspd_client_fixtures.PARCEL_BY_CADASTRAL_ID == obj
        request = httpretty.last_request()
        assert {'thematicSearchId': ['1'], 'query': [cadastral_id]} == request.querystring
        assert self.NSPD_REFERER == request.headers['Referer']

    @httpretty.activate
    def test_get_building_by_coordinates(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_BUILDINGS_WMS_URL,
            body=nspd_client_fixtures.BUILDING_BY_COORDINATES_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = NSPDAPIClient()
        obj = api_client.get_building_by_coordinates(lat=55.828952, long=49.097076, limit=1)

        assert nspd_client_fixtures.BUILDING_BY_COORDINATES == obj
        request = httpretty.last_request()
        query = {key: value[0] for key, value in request.querystring.items()}
        assert 'GetFeatureInfo' == query['REQUEST']
        assert '36049' == query['LAYERS'] == query['QUERY_LAYERS']
        assert '1' == query['FEATURE_COUNT']
        min_x, min_y, max_x, max_y = map(float, query['BBOX'].split(','))
        # the point in EPSG:3857
        assert (min_x + max_x) / 2 == pytest.approx(5465461.50, abs=0.01)
        assert (min_y + max_y) / 2 == pytest.approx(7524439.92, abs=0.01)
        assert self.NSPD_REFERER == request.headers['Referer']

    @httpretty.activate
    def test_get_building_by_cadastral_id(self):
        cadastral_id = '77:01:0001005:2106'
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_SEARCH_URL,
            body=nspd_client_fixtures.BUILDING_BY_CADASTRAL_ID_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = NSPDAPIClient()
        obj = api_client.get_building_by_cadastral_id(cadastral_id)

        assert nspd_client_fixtures.BUILDING_BY_CADASTRAL_ID == obj
        request = httpretty.last_request()
        assert {'thematicSearchId': ['1'], 'query': [cadastral_id]} == request.querystring
        assert self.NSPD_REFERER == request.headers['Referer']

    @httpretty.activate
    def test_get_object(self):
        cadastral_id = '77:05:0007007:4926'
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_SEARCH_URL,
            body=nspd_client_fixtures.OBJECT_BY_ID_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = NSPDAPIClient()
        obj = api_client.get_object(cadastral_id)

        assert nspd_client_fixtures.OBJECT_BY_ID == obj
        request = httpretty.last_request()
        assert {'thematicSearchId': ['1'], 'query': [cadastral_id]} == request.querystring
        assert self.NSPD_REFERER == request.headers['Referer']

    @httpretty.activate
    def test_get_object_not_found(self):
        not_found = {'code': 204, 'message': 'no objects found'}
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_SEARCH_URL, status=404,
            body=json.dumps(not_found), content_type=self.CONTENT_TYPE_JSON)

        api_client = NSPDAPIClient()

        with pytest.raises(requests.HTTPError) as exc_info:
            api_client.get_object('77:17:0000000:11471')
        assert 404 == exc_info.value.response.status_code

    @httpretty.activate
    def test_get_parcel_by_coordinates_blocked_by_waf(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.NSPD_PARCELS_WMS_URL, status=403,
            body='<html><body>Request blocked. Rule: 123</body></html>',
            content_type='text/html')

        api_client = NSPDAPIClient()

        with pytest.raises(requests.HTTPError) as exc_info:
            api_client.get_parcel_by_coordinates(lat=55.761, long=37.6096)
        assert 403 == exc_info.value.response.status_code
