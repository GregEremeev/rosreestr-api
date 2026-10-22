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


PARCEL_BY_CADASTRAL_ID = {
    'data': {
        'type': 'FeatureCollection',
        'features': [
            {
                'id': 291075836,
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [
                        [
                            [7246785.665908192, 7837657.655958384],
                            [7246789.1965312455, 7837604.137466149],
                            [7246905.274968546, 7837611.364314863],
                            [7246901.744892771, 7837664.901455792],
                            [7246785.665908192, 7837657.655958384]
                        ]
                    ],
                    'crs': {
                        'type': 'name',
                        'properties': {
                            'name': 'EPSG:3857'
                        }
                    }
                },
                'properties': {
                    'cadastralDistrictsCode': 72,
                    'category': 36368,
                    'categoryName': 'Земельные участки ЕГРН',
                    'descr': '72:17:1502001:499',
                    'externalKey': '72:17:1502001:499',
                    'interactionId': 273550233,
                    'label': '72:17:1502001:499',
                    'options': {
                        'area': None,
                        'cad_num': '72:17:1502001:499',
                        'cost_application_date': '2024-09-12',
                        'cost_approvement_date': '',
                        'cost_determination_date': '2022-01-01',
                        'cost_index': 151.06,
                        'cost_registration_date': '2024-09-20',
                        'cost_value': 274627.08,
                        'declared_area': None,
                        'determination_couse': 'Акт бюджетного учреждения, созданного субъектом Российской Федерации, об определении кадастровой стоимости в соответствии со статьей 16 Закона 237-ФЗ',
                        'land_record_category_type': 'Земли населенных пунктов',
                        'land_record_reg_date': '2024-09-12',
                        'land_record_subtype': 'Землепользование',
                        'land_record_type': 'Земельный участок',
                        'ownership_type': None,
                        'permitted_use_established_by_document': 'Для индивидуального жилищного строительства',
                        'quarter_cad_number': '72:17:1502001',
                        'readable_address': 'Тюменская область, Тюменский район, д. Нариманова',
                        'specified_area': 1818,
                        'status': 'Учтенный'
                    },
                    'subcategory': 5,
                    'systemInfo': {
                        'inserted': '2024-09-17T13:57:24.247083',
                        'insertedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79',
                        'updated': '2026-10-18T12:39:18.175413',
                        'updatedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79'
                    }
                }
            }
        ]
    },
    'meta': [
        {
            'totalCount': 1,
            'categoryId': 36368
        }
    ]
}
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
