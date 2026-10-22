import json


OBJECTS_BY_ADDRESS = [
    {
        'cadnum': '77:05:0007007:4926',
        'full_name': 'Российская Федерация, г. Москва, вн.тер.г. муниципальный округ Чертаново Центральное, ул. Красного Маяка, д. 22 к. 2, кв. 187',
        'actual': True,
        'type': 'FLAT'
    },
    {
        'cadnum': '77:05:0007007:5142',
        'full_name': 'Российская Федерация, г. Москва, вн.тер.г. муниципальный округ Чертаново Центральное, ул. Красного Маяка, д. 22 к. 1, кв. 187',
        'actual': True,
        'type': 'FLAT'
    }
]
OBJECTS_BY_ADDRESS_RESPONSE = json.dumps(OBJECTS_BY_ADDRESS).encode('utf-8')


OBJECT_BY_ID = {
    'data': {
        'type': 'FeatureCollection',
        'features': [
            {
                'id': 3225793942,
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [4183234.922503614, 7481488.382915592],
                    'crs': {
                        'type': 'name',
                        'properties': {
                            'name': 'EPSG:3857'
                        }
                    }
                },
                'properties': {
                    'category': 37163,
                    'categoryName': 'Помещения',
                    'options': {
                        'area': 76.7,
                        'cad_number': '77:05:0007007:4926',
                        'cancel_date': None,
                        'common_data_status': 'Ранее учтенный',
                        'common_property': 'false',
                        'cost_index': 212482.31,
                        'cost_value': 16297393.18,
                        'facility_cad_number': None,
                        'floor': [
                            '14/Этаж'
                        ],
                        'geocoderObject': True,
                        'objdocId': 3225793942,
                        'ownership_type': 'Частная',
                        'params_type': 'Квартира',
                        'parent_cad_number': '77:05:0007007:1045',
                        'purpose': 'Жилое',
                        'readable_address': 'Российская Федерация, г. Москва, вн.тер.г. муниципальный округ Чертаново Центральное, ул. Красного Маяка, д. 22 к. 2, кв. 187',
                        'registersId': 36455,
                        'registration_date': '2012-05-26T00:00:00Z',
                        'removed_GCU': False,
                        'service_common_property': None,
                        'type': 'Помещение'
                    }
                }
            }
        ]
    },
    'meta': [
        {
            'totalCount': 1,
            'categoryId': 37163
        }
    ]
}
OBJECT_BY_ID_RESPONSE = json.dumps(OBJECT_BY_ID).encode('utf-8')


