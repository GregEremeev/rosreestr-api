import json


OBJECT_BY_COORDINATES = {
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
OBJECT_BY_COORDINATES_RESPONSE = json.dumps(OBJECT_BY_COORDINATES).encode('utf-8')


OBJECT_BY_CADASTRAL_ID = OBJECT_BY_COORDINATES
OBJECT_BY_CADASTRAL_ID_RESPONSE = json.dumps(OBJECT_BY_CADASTRAL_ID).encode('utf-8')
