import json


PARCEL_BY_COORDINATES = {
    'features': [
        {'attrs': {
            'address': 'Москва, п Сосенское, д Столбово, з/у 3/1',
            'cn': '77:17:0000000:11471',
            'id': '77:17:0:11471'},
         'center': {'x': 4172677.635874182, 'y': 7467970.62866414},
         'extent': {
             'xmax': 4173270.1685763774,
             'xmin': 4171926.086091824,
             'ymax': 7468416.583502886,
             'ymin': 7467322.552103312
         },
         'sort': 7717000000011471,
         'type': 1}
    ],
    'note': '',
    'status': 200,
    'total': None
}
PARCEL_BY_COORDINATES_RESPONSE = json.dumps(PARCEL_BY_COORDINATES).encode('utf-8')


PARCEL_BY_CADASTRAL_ID = PARCEL_BY_COORDINATES
PARCEL_BY_CADASTRAL_ID_RESPONSE = json.dumps(PARCEL_BY_CADASTRAL_ID).encode('utf-8')


BUILDING_BY_COORDINATES = {
  'features': [
    {
      'attrs': {
        'address': 'Российская Федерация, Тульская область, г.Тула, ул. 1-ая Хомутовка',
        'cn': '71:00:000000:112278',
        'id': '71:0:0:112278'
      },
      'center': {
        'x': 4187644.2574798283,
        'y': 7202894.7063751975
      },
      'extent': {
        'xmax': 4190910.7296789056,
        'xmin': 4184226.322656533,
        'ymax': 7205638.943976473,
        'ymin': 7199935.937776311
      },
      'sort': 71000000000112278,
      'type': 5
    }
  ],
  'note': '',
  'status': 200,
  'total': None
}
BUILDING_BY_COORDINATES_RESPONSE = json.dumps(BUILDING_BY_COORDINATES).encode('utf-8')

BUILDING_BY_CADASTRAL_ID = BUILDING_BY_COORDINATES
BUILDING_BY_CADASTRAL_ID_RESPONSE = json.dumps(BUILDING_BY_CADASTRAL_ID).encode('utf-8')
