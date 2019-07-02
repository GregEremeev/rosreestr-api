import pytest
import httpretty

from rosreestr_api.tests import rosreestr_client_fixtures, pkk5_client_fixtures
from rosreestr_api.clients import (
    AddressWrapper, RosreestrAPIClient, PKK5RosreestrAPIClient)


def test_fill_address_wrapper_without_macro_region():
    with pytest.raises(ValueError):
        AddressWrapper(
            region_id='145296000000', street_name='Красного маяка',
            house_number='22', house_building='2')


def test_fill_address_wrapper_without_region():
    with pytest.raises(ValueError):
        AddressWrapper(
            street_name='Красного маяка', macro_region_name='Москва',
            house_number='22', house_building='2')


def test_fill_address_wrapper():
    AddressWrapper(
        macro_region_id='145000000000', region_id='145296000000',
        street_name='Красного маяка', house_number='22', house_building='2')


class TestRosreestrAPIClient:

    BASE_URL = 'http://rosreestr.ru/api/online'
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

    CONTENT_TYPE_JSON = 'application/json'

    @httpretty.activate
    def test_get_macro_regions(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.MACRO_REGIONS_URL, body=rosreestr_client_fixtures.MACRO_REGIONS_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()

        assert rosreestr_client_fixtures.MACRO_REGIONS == api_client.macro_regions

    @httpretty.activate
    def test_get_regions(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.MACRO_REGIONS_URL, body=rosreestr_client_fixtures.MACRO_REGIONS_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)
        httpretty.register_uri(
            method=httpretty.GET, uri=self.REGIONS_URL.format(rosreestr_client_fixtures.MACRO_REGION_ID_1),
            body=rosreestr_client_fixtures.MACRO_REGION_TO_REGION_1_RESPONSE, content_type=self.CONTENT_TYPE_JSON)
        httpretty.register_uri(
            method=httpretty.GET, uri=self.REGIONS_URL.format(rosreestr_client_fixtures.MACRO_REGION_ID_2),
            body=rosreestr_client_fixtures.MACRO_REGION_TO_REGION_2_RESPONSE, content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()

        assert rosreestr_client_fixtures.MACRO_REGIONS_TO_REGIONS == api_client.macro_regions_to_regions

    @httpretty.activate
    def test_get_region_types(self):
        httpretty.register_uri(
            method=httpretty.GET, uri=self.REGION_TYPES_URL.format(rosreestr_client_fixtures.REGION_ID),
            body=rosreestr_client_fixtures.REGION_TYPES_RESPONSE, content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()

        assert rosreestr_client_fixtures.REGION_TYPES == api_client.get_region_types(rosreestr_client_fixtures.REGION_ID)

    @httpretty.activate
    def test_get_objects_by_right(self):
        region_number = '177'
        right_id = '50-50-21-042-2012-234'
        url = self.SEARCH_OBJECTS_BY_RIGHT_URL.format(region_number, right_id)
        httpretty.register_uri(
            method=httpretty.GET, uri=url, body=rosreestr_client_fixtures.RIGHT_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()
        objects = api_client.get_objects_by_right(region_number, right_id)

        assert rosreestr_client_fixtures.RIGHT_OBJECTS == objects

    @httpretty.activate
    def test_get_objects_by_address(self):
        macro_region_id = '145000000000'
        region_id = '145296000000'
        street_name = 'Красного маяка'
        house_number = '22'
        house_building = '2'
        apartment = '187'
        address = AddressWrapper(
            macro_region_id=macro_region_id, region_id=region_id, apartment=apartment,
            street_name=street_name, house_number=house_number, house_building=house_building)
        url = self.SEARCH_OBJECTS_BY_ADDRESS_URL.format(
            macro_region_id=macro_region_id, region_id=region_id,
            street_name=street_name, house_number=house_number, house_building=house_building,
            apartment=apartment, house_structure='')
        httpretty.register_uri(
            method=httpretty.GET, uri=url, body=rosreestr_client_fixtures.OBJECTS_BY_ADDRESS_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()
        objects = api_client.get_objects_by_address(address)

        assert rosreestr_client_fixtures.OBJECTS_BY_ADDRESS == objects

    @httpretty.activate
    def test_get_object(self):
        object_id = '177_385900460001'
        url = self.SEARCH_DETAILED_OBJECT_BY_ID.format(object_id)
        httpretty.register_uri(
            method=httpretty.GET, uri=url, body=rosreestr_client_fixtures.OBJECT_BY_ID_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = RosreestrAPIClient()
        obj = api_client.get_object(object_id)

        assert rosreestr_client_fixtures.OBJECT_BY_ID == obj


class TestPKK5RosreestrAPIClient:

    BASE_URL = 'https://pkk5.rosreestr.ru/api'
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

    CONTENT_TYPE_JSON = 'application/json'

    @httpretty.activate
    def test_get_parcel_by_coordinates(self):
        search_params = {
            'lat': 55.542, 'long': 37.483,
            'limit': 11, 'tolerance': 2}
        url = self.SEARCH_PARCEL_BY_COORDINATES_URL.format(**search_params)
        httpretty.register_uri(
            method=httpretty.GET, uri=url,
            body=pkk5_client_fixtures.PARCEL_BY_COORDINATES_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = PKK5RosreestrAPIClient()
        obj = api_client.get_parcel_by_coordinates(**search_params)

        assert pkk5_client_fixtures.PARCEL_BY_COORDINATES == obj

    @httpretty.activate
    def test_get_parcel_by_cadastral_id(self):
        search_params = {
            'cadastral_id': '77:17:0000000:11471', 'limit': 11, 'tolerance': 2}
        url = self.SEARCH_PARCEL_BY_CADASTRAL_ID_URL.format(**search_params)
        httpretty.register_uri(
            method=httpretty.GET, uri=url,
            body=pkk5_client_fixtures.PARCEL_BY_CADASTRAL_ID_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = PKK5RosreestrAPIClient()
        obj = api_client.get_parcel_by_cadastral_id(**search_params)

        assert pkk5_client_fixtures.PARCEL_BY_CADASTRAL_ID == obj

    @httpretty.activate
    def test_get_building_by_coordinates(self):
        search_params = {
            'lat': 54.16829, 'long': 37.59876,
            'limit': 1, 'tolerance': 170}
        url = self.SEARCH_BUILDING_BY_COORDINATES_URL.format(**search_params)
        httpretty.register_uri(
            method=httpretty.GET, uri=url,
            body=pkk5_client_fixtures.BUILDING_BY_COORDINATES_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = PKK5RosreestrAPIClient()
        obj = api_client.get_building_by_coordinates(**search_params)

        assert pkk5_client_fixtures.BUILDING_BY_COORDINATES == obj

    @httpretty.activate
    def test_get_building_by_cadastral_id(self):
        search_params = {
            'cadastral_id': '71:00:000000:112278', 'limit': 1, 'tolerance': 170}
        url = self.SEARCH_BUILDING_BY_CADASTRAL_ID_URL.format(**search_params)
        httpretty.register_uri(
            method=httpretty.GET, uri=url,
            body=pkk5_client_fixtures.BUILDING_BY_CADASTRAL_ID_RESPONSE,
            content_type=self.CONTENT_TYPE_JSON)

        api_client = PKK5RosreestrAPIClient()
        obj = api_client.get_building_by_cadastral_id(**search_params)

        assert pkk5_client_fixtures.BUILDING_BY_CADASTRAL_ID == obj
