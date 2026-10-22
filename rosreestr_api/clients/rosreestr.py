import logging
import math

import requests
from fake_useragent import UserAgent

from rosreestr_api.clients.http import RosreestrHTTPClient

logger = logging.getLogger(__name__)

# WGS 84 semi-major axis in metres, used by EPSG:3857
EARTH_RADIUS = 6378137


class RosreestrAPIClient:

    SEARCH_OBJECTS_BY_ADDRESS_URL = 'https://lk.rosreestr.ru/account-back/address/search'

    def __init__(self, timeout=5, keep_alive=False):
        self._http_client = RosreestrHTTPClient(
            timeout=timeout,
            keep_alive=keep_alive,
            default_headers={'User-Agent': UserAgent().random}
        )

    def _get_response_body(self, response: requests.Response):
        status_code = response.status_code
        if status_code >= 400:
            response.raise_for_status()
        elif status_code == 204:
            logger.info('There was an empty response body')
            return ''
        else:
            return response.json()

    def get_objects_by_address(self, address: str):
        # rosreestr.gov.ru/api/online was replaced by lk.rosreestr.ru, whose
        # address search is free text, e.g. 'Москва, ул Красного Маяка, д 22, к 2, кв 187'.
        # It returns at most 100 objects and includes near matches.
        logger.info(f'Trying to download rosreestr objects, address: {address}')
        response = self._http_client.get(self.SEARCH_OBJECTS_BY_ADDRESS_URL, params={'term': address})

        objects = self._get_response_body(response)
        if objects:
            logger.info('Rosreestr objects were downloaded')
            logger.info(f'Number of rosreestr objects: {len(objects)}')
            return objects
        else:
            return []

    def get_object(self, cadastral_id: str):
        # rosreestr.gov.ru/api/online was shut down; nspd.gov.ru has the same
        # details for parcels, buildings and premises, by the full cadastral id only
        params = {
            'thematicSearchId': NSPDAPIClient.NSPD_REAL_ESTATE_THEMATIC_SEARCH_ID,
            'query': cadastral_id,
        }
        headers = {'Referer': NSPDAPIClient.NSPD_REFERER}
        logger.info(f'Trying to download detailed object, cadastral_id: {cadastral_id}')
        response = self._http_client.get(
            NSPDAPIClient.NSPD_SEARCH_URL, params=params, headers=headers)
        logger.info(f'Detailed object was downloaded, cadastral_id: {cadastral_id}')
        return self._get_response_body(response)


class NSPDAPIClient:

    # about rosreestr's coordinate system
    # http://holmogori.ru/govinfo/rosreestr/media/2017/4/12/o-primenyaemyih-sistemah-koordinat-dlya-vedeniya-egrn/
    # about МСК
    # https://geostart.ru/post/312

    # pkk.rosreestr.ru was replaced by nspd.gov.ru on 23.12.2024
    NSPD_BASE_URL = 'https://nspd.gov.ru/api'
    # nspd's WAF rejects API requests without a Referer pointing to the map page
    NSPD_REFERER = 'https://nspd.gov.ru/map?thematic=PKK'
    NSPD_SEARCH_URL = NSPD_BASE_URL + '/geoportal/v2/search/geoportal'
    NSPD_REAL_ESTATE_THEMATIC_SEARCH_ID = 1
    SEARCH_PARCEL_BY_CADASTRAL_ID_URL = NSPD_SEARCH_URL
    SEARCH_BUILDING_BY_CADASTRAL_ID_URL = NSPD_SEARCH_URL
    NSPD_WMS_URL = NSPD_BASE_URL + '/aeggis/v3/{layer_id}/wms'
    NSPD_PARCELS_LAYER_ID = 36048
    NSPD_BUILDINGS_LAYER_ID = 36049
    SEARCH_PARCEL_BY_COORDINATES_URL = NSPD_WMS_URL.format(layer_id=NSPD_PARCELS_LAYER_ID)
    SEARCH_BUILDING_BY_COORDINATES_URL = NSPD_WMS_URL.format(layer_id=NSPD_BUILDINGS_LAYER_ID)
    # GetFeatureInfo asks what lies under the centre pixel of a small map
    # image around the point; nspd works in EPSG:3857 only
    NSPD_FEATURE_INFO_IMAGE_SIZE = 512
    NSPD_FEATURE_INFO_BBOX_HALF_SIZE = 10  # metres in EPSG:3857

    def __init__(self, timeout=5, keep_alive=False):
        self._http_client = RosreestrHTTPClient(
            timeout=timeout,
            keep_alive=keep_alive,
            default_headers={'User-Agent': UserAgent().random, 'Referer': self.NSPD_REFERER}
        )

    def get_parcel_by_coordinates(self, *, lat, long, limit=11) -> dict:
        return self._get_feature_info(
            self.SEARCH_PARCEL_BY_COORDINATES_URL, self.NSPD_PARCELS_LAYER_ID,
            lat=lat, long=long, limit=limit)

    def get_parcel_by_cadastral_id(self, cadastral_id) -> dict:
        return self._search_by_cadastral_id(self.SEARCH_PARCEL_BY_CADASTRAL_ID_URL, cadastral_id)

    def get_building_by_cadastral_id(self, cadastral_id) -> dict:
        return self._search_by_cadastral_id(self.SEARCH_BUILDING_BY_CADASTRAL_ID_URL, cadastral_id)

    def get_building_by_coordinates(self, *, lat, long, limit=11) -> dict:
        return self._get_feature_info(
            self.SEARCH_BUILDING_BY_COORDINATES_URL, self.NSPD_BUILDINGS_LAYER_ID,
            lat=lat, long=long, limit=limit)

    def _search_by_cadastral_id(self, url, cadastral_id) -> dict:
        params = {
            'thematicSearchId': self.NSPD_REAL_ESTATE_THEMATIC_SEARCH_ID,
            'query': cadastral_id,
        }
        return self._http_client.get(url, params=params).json()

    def _get_feature_info(self, url, layer_id, *, lat, long, limit) -> dict:
        x, y = _wgs84_to_web_mercator(lat=lat, long=long)
        half_size = self.NSPD_FEATURE_INFO_BBOX_HALF_SIZE
        image_size = self.NSPD_FEATURE_INFO_IMAGE_SIZE
        params = {
            'SERVICE': 'WMS',
            'VERSION': '1.3.0',
            'REQUEST': 'GetFeatureInfo',
            'LAYERS': layer_id,
            'QUERY_LAYERS': layer_id,
            'STYLES': '',
            # nspd responds with 500 when FORMAT is missing
            'FORMAT': 'image/png',
            'INFO_FORMAT': 'application/json',
            'FEATURE_COUNT': limit,
            'CRS': 'EPSG:3857',
            'BBOX': f'{x - half_size},{y - half_size},{x + half_size},{y + half_size}',
            'WIDTH': image_size,
            'HEIGHT': image_size,
            'I': image_size // 2,
            'J': image_size // 2,
        }
        return self._http_client.get(url, params=params).json()


def _wgs84_to_web_mercator(*, lat, long):
    # https://epsg.io/3857, spherical Mercator projection of WGS 84 (EPSG:4326)
    x = math.radians(long) * EARTH_RADIUS
    y = math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) * EARTH_RADIUS
    return x, y
