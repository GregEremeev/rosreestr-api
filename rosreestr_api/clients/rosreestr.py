import logging
from dataclasses import dataclass
from urllib.parse import quote_plus

import requests
from fake_useragent import UserAgent

from rosreestr_api.clients.http import HTTPClient


logger = logging.getLogger(__name__)


@dataclass
class AddressWrapper:

    street_name: str
    house_number: str
    macro_region_id: str = ''
    region_id: str = ''
    house_building: str = ''
    house_structure: str = ''
    apartment: str = ''
    macro_region_type: str = ''

    region_name: str = ''
    macro_region_name: str = ''

    def __post_init__(self):
        is_region_filled = self.region_name or self.region_id
        is_macro_region_filled = self.macro_region_name or self.macro_region_id
        if not (is_macro_region_filled and is_region_filled):
            raise ValueError('You have to provide region and macro region values')


class RosreestrAPIClient:

    BASE_URL = 'https://rosreestr.gov.ru/api/online'
    MACRO_REGIONS_URL = f'{BASE_URL}/macro_regions/'
    REGIONS_URL = f'{BASE_URL}/regions/' + '{}/'
    REGION_TYPES_URL = f'{BASE_URL}/region_types/' + '{}/'
    SEARCH_OBJECTS_BY_RIGHT_URL = f'{BASE_URL}/right/' + '{}/{}/'
    SEARCH_OBJECTS_BY_ADDRESS_URL = (
        f'{BASE_URL}/address/fir_objects/'
        + '?macroRegionId={macro_region_id}&regionId={region_id}'
        + '&street={street_name}&house={house_number}&building={house_building}'
        + '&structure={house_structure}&apartment={apartment}')
    SEARCH_DETAILED_OBJECT_BY_ID = f'{BASE_URL}/fir_object/' + '{}/'

    REPUBLIC = 'республика'

    def __init__(self, timeout=5, keep_alive=False):
        self._http_client = HTTPClient(
            timeout=timeout,
            keep_alive=keep_alive,
            default_headers={'User-Agent': UserAgent().random}
        )
        self._macro_regions = None
        self._macro_regions_to_regions = None

    def _get_response_body(self, response: requests.Response):
        status_code = response.status_code
        if status_code >= 400:
            response.raise_for_status()
        elif status_code == 204:
            logger.info('There was an empty response body')
            return ''
        else:
            return response.json()

    def _get_macro_region_id(self, macro_region_name: str):
        for macro_region in self.macro_regions:
            if macro_region['name'].lower() == macro_region_name.lower():
                return macro_region['id']
        raise ValueError(
            f'There was not found suitable macro region '
            f'for macro region name - `{macro_region_name}`')

    def _get_region_id(self, region_name: str, macro_region_name: str) -> int:
        macro_region_id = self._get_macro_region_id(macro_region_name)
        for region in self.macro_regions_to_regions[macro_region_id]:
            if region['name'].lower() == region_name.lower():
                return region['id']
        raise ValueError(
            f'There was not found suitable region_id for '
            f'region name - `{region_name}` and macro region '
            f'name - `{macro_region_name}`')

    @property
    def macro_regions(self):
        if not self._macro_regions:
            self._macro_regions = self._http_client.get(self.MACRO_REGIONS_URL).json()
            logger.info('Macro regions were downloaded')
        return self._macro_regions

    @property
    def macro_regions_to_regions(self):
        if not self._macro_regions_to_regions:
            self._macro_regions_to_regions = {}
            for macro_region in self.macro_regions:
                response = self._http_client.get(
                    self.REGIONS_URL.format(macro_region['id']))
                self._macro_regions_to_regions[
                    macro_region['id']] = response.json()
            logger.info('Regions were downloaded')
        return self._macro_regions_to_regions

    def get_region_types(self, region_id: str):
        response = self._http_client.get(self.REGION_TYPES_URL.format(region_id))
        return self._get_response_body(response)

    def get_objects_by_right(self, region_number: str, right_number: str):
        url = self.SEARCH_OBJECTS_BY_RIGHT_URL.format(region_number, quote_plus(right_number))
        return self._get_response_body(self._http_client.get(url))

    def get_objects_by_address(self, address_wrapper: AddressWrapper):
        macro_region_id = address_wrapper.macro_region_id
        if not address_wrapper.macro_region_id:
            macro_region_name = address_wrapper.macro_region_name.lower()
            if macro_region_name.endswith('ая'):
                macro_region_name = macro_region_name + ' область'
            elif macro_region_name.endswith('ий'):
                macro_region_name = macro_region_name + ' край'
            elif address_wrapper.macro_region_type.lower() == self.REPUBLIC:
                macro_region_name = f'{self.REPUBLIC} {macro_region_name}'
            macro_region_id = self._get_macro_region_id(macro_region_name)

        region_id = address_wrapper.region_id
        if not region_id:
            region_id = self._get_region_id(
                address_wrapper.region_name, address_wrapper.macro_region_name)

        search_objects_url = self.SEARCH_OBJECTS_BY_ADDRESS_URL.format(
            macro_region_id=macro_region_id, region_id=region_id,
            street_name=address_wrapper.street_name,
            house_number=address_wrapper.house_number,
            house_building=address_wrapper.house_building,
            house_structure=address_wrapper.house_structure,
            apartment=address_wrapper.apartment)

        logger.info(f'search_objects_url: {search_objects_url}')
        logger.info('Trying to download rosreestr objects')
        response = self._http_client.get(search_objects_url)

        objects = self._get_response_body(response)
        if objects:
            logger.info('Rosreestr objects were downloaded')
            logger.info(f'Number of rosreestr objects: {len(objects)}')
            return objects
        else:
            return []

    def get_object(self, obj_id: str):
        obj_id = _strip_cadastral_id(obj_id)
        url = self.SEARCH_DETAILED_OBJECT_BY_ID.format(obj_id)
        logger.info(f'Trying to download detailed object, object_id: {obj_id}')
        response = self._http_client.get(url)
        logger.info(f'Detailed object was downloaded, object_id: {obj_id}')
        return self._get_response_body(response)


class PKKRosreestrAPIClient:

    # about rosreestr's coordinate system
    # http://holmogori.ru/govinfo/rosreestr/media/2017/4/12/o-primenyaemyih-sistemah-koordinat-dlya-vedeniya-egrn/
    # about МСК
    # https://geostart.ru/post/312

    BASE_URL = 'https://pkk.rosreestr.ru/api'
    SEARCH_OBJECT_BY_CADASTRAL_ID = (
        BASE_URL + '/features/{object_type}?text={{cadastral_id}}&limit={{limit}}&'
        + 'tolerance={{tolerance}}')
    SEARCH_OBJECT_BY_COORDINATES = (
        BASE_URL + '/features/{object_type}?text={{lat}}%20{{long}}&limit={{limit}}&'
        + 'tolerance={{tolerance}}')
    SEARCH_BUILDING_BY_COORDINATES_URL = SEARCH_OBJECT_BY_COORDINATES.format(object_type=5)
    SEARCH_BUILDING_BY_CADASTRAL_ID_URL = SEARCH_OBJECT_BY_CADASTRAL_ID.format(object_type=5)
    SEARCH_PARCEL_BY_COORDINATES_URL = SEARCH_OBJECT_BY_COORDINATES.format(object_type=1)
    SEARCH_PARCEL_BY_CADASTRAL_ID_URL = SEARCH_OBJECT_BY_CADASTRAL_ID.format(object_type=1)

    def __init__(self, timeout=5, keep_alive=False):
        self._http_client = HTTPClient(
            timeout=timeout,
            keep_alive=keep_alive,
            default_headers={'User-Agent': UserAgent().random}
        )

    def get_parcel_by_coordinates(self, *, lat, long, limit=11, tolerance=2) -> dict:
        url = self.SEARCH_PARCEL_BY_COORDINATES_URL.format(
            lat=lat, long=long, limit=limit, tolerance=tolerance)
        return self._http_client.get(url).json()

    def get_parcel_by_cadastral_id(self, cadastral_id, limit=11, tolerance=2) -> dict:
        url = self.SEARCH_PARCEL_BY_CADASTRAL_ID_URL.format(
            cadastral_id=cadastral_id, limit=limit, tolerance=tolerance)
        return self._http_client.get(url).json()

    def get_building_by_cadastral_id(self, cadastral_id, limit=11, tolerance=2) -> dict:
        url = self.SEARCH_BUILDING_BY_CADASTRAL_ID_URL.format(
            cadastral_id=cadastral_id, limit=limit, tolerance=tolerance)
        return self._http_client.get(url).json()

    def get_building_by_coordinates(self, *, lat, long, limit=11, tolerance=2) -> dict:
        url = self.SEARCH_BUILDING_BY_COORDINATES_URL.format(
            lat=lat, long=long, limit=limit, tolerance=tolerance)
        return self._http_client.get(url).json()


def _strip_cadastral_id(cadastral_id):
    stripped_cadastral_id = []
    cadastral_id = cadastral_id.split(':')
    for part in cadastral_id:
        if part:
            stripped_cadastral_id.append(part[:-1].lstrip('0') + part[-1])
    return ':'.join(stripped_cadastral_id)
