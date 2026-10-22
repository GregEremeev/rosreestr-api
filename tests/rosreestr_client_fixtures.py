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
