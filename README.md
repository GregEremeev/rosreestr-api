## rosreestr-api

#### `rosreestr-api` is an BSD licensed library written in Python. It will be helpful for you if you need to work with rosreestr.ru/api or pkk5.rosreestr.ru/api to obtain info related to realty objects.

### Quick start

1 install the library:
```bash
pip install rosreestr-api
```

2 Different ways how to get basic info about realty objects:
```python
from rosreestr_api.clients import RosreestrAPIClient, AddressWrapper

api_client = RosreestrAPIClient()

# get objects by address
macro_regions = api_client.macro_regions
moscow_m_reg_id = [m['id'] for m in macro_regions if m['name'] == 'Москва'][0]
m_regs_to_regs = api_client.macro_regions_to_regions
moscow_regions = [m_regs_to_regs[reg_id] for reg_id in m_regs_to_regs if reg_id == moscow_m_reg_id][0]
region_id = [r['id'] for r in moscow_regions if r['name'] == 'Южный'][0]

address_with_ids = AddressWrapper(
    macro_region_id=moscow_m_reg_id, region_id=region_id,
    street_name='Красного маяка', house_number=22, house_building=2,
    apartment=187)
address_with_names = AddressWrapper(
    macro_region_name='Москва', region_name='Южный',
    street_name='Красного маяка', house_number=22, house_building=2,
    apartment=187)
api_client.get_objects_by_address(address_with_ids)
api_client.get_objects_by_address(address_with_names)

# get object by id (the same as cadastral id for parcel objects, look at `objectId` key)
api_client.get_object('77:5:7007:4926')

# get objects by region number and right number
api_client.get_objects_by_right(region_number=177, right_number='50-50-21/042/2012-234')

# get region types by region id
api_client.get_region_types(region_id=region_id)
```

3 Different ways how to get geo info about realty objects:
```python
from rosreestr_api.clients import PKK5RosreestrAPIClient

api_client = PKK5RosreestrAPIClient()

# get objects by cadastral id
api_client.get_object_by_cadastral_id('77:17:0000000:11471')

# get objects by coordinates
api_client.get_object_by_coordinates(lat=55.542, long=37.483)
```
