import json


MACRO_REGION_ID_1 = 199000000000
REGION_ID = 199401000000
REGION_1_VALUE = [
    {'id': REGION_ID, 'name': 'Биробиджан'},
    {'id': 199230000000, 'name': 'Смидовичский'}
]
MACRO_REGION_TO_REGION_1_RESPONSE = json.dumps(REGION_1_VALUE).encode('utf-8')


MACRO_REGION_ID_2 = 39200000000000
REGION_2_VALUE = [
    {"id": 39200000000600, "name": "Андреевка"},
    {"id": 39200000000800, "name": "Верхнесадовое"},
    {"id": 39200000000200, "name": "Вишневое"}
]
MACRO_REGION_TO_REGION_2_RESPONSE = json.dumps(REGION_2_VALUE).encode('utf-8')


MACRO_REGIONS_TO_REGIONS = {
    MACRO_REGION_ID_2: REGION_2_VALUE,
    MACRO_REGION_ID_1: REGION_1_VALUE
}


MACRO_REGIONS = [
    {'id': MACRO_REGION_ID_1, 'name': 'Еврейская А.обл.'},
    {'id': MACRO_REGION_ID_2, 'name': 'Севастополь'}]
MACRO_REGIONS_RESPONSE = json.dumps(MACRO_REGIONS).encode('utf-8')


REGION_TYPES = [
    {"webType": "set15", "typeDesc": "Поселок сельского типа"},
    {"webType": "set22", "typeDesc": "Село"},
    {"webType": "set5", "typeDesc":"Деревня"}
]
REGION_TYPES_RESPONSE = json.dumps(REGION_TYPES).encode('utf-8')


RIGHT_OBJECTS = [
    {"objectId": "177_1357453010001", "srcObject": 2, "regionKey":177, "objectType": None,
     "objectCn": "77:17:0120316:9111", "objectCon": None, "subjectId": 145000000000,
     "regionId": 145297000000, "settlementId": 145297574000, "street": None, "house": "||",
     "addressNotes": "г.Москва, п.Сосенское, пос.Коммунарка",
     "okato": None, "apartment": None, "nobjectCn": "77:17:120316:9111",
     "nobjectCon": None}
]
RIGHT_RESPONSE = json.dumps(RIGHT_OBJECTS).encode('utf-8')


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


