## rosreestr-api

#### `rosreestr-api` is an BSD licensed library written in Python. It will be helpful for you if you need to work with rosreestr.ru/api or nspd.gov.ru/api (formerly pkk.rosreestr.ru) to obtain info related to realty objects.

### Quick start

1 install the library:
```bash
pip install rosreestr-api
```

2 Different ways how to get basic info about realty objects:
```python
from rosreestr_api.clients.rosreestr import RosreestrAPIClient

api_client = RosreestrAPIClient()

# get objects by address: returns up to 100 objects with `cadnum`, `full_name`,
# `actual` and `type` (OKS, PARCEL or FLAT), near matches included
api_client.get_objects_by_address('Москва, ул Красного Маяка, д 22, к 2, кв 187')

# get object by id (the same as cadastral id for parcel objects, look at `objectId` key)
api_client.get_object('77:5:7007:4926')

# get objects by region number and right number
api_client.get_objects_by_right(region_number=177, right_number='50-50-21/042/2012-234')

# get region types by region id
api_client.get_region_types(region_id='145296000000')
```

3 Different ways how to get geo info about realty objects:
```python
from rosreestr_api.clients.rosreestr import PKKRosreestrAPIClient

api_client = PKKRosreestrAPIClient()

# get building by cadastral id
api_client.get_building_by_cadastral_id('16:50:110108:2815')

# get parcel by cadastral id
api_client.get_parcel_by_cadastral_id('72:17:1502001:499')

# get parcel by coordinates
api_client.get_parcel_by_coordinates(lat=55.542, long=37.483)

# get building by coordinates
api_client.get_building_by_coordinates(lat=55.828952, long=49.097076)
```
