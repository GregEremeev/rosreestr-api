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
        'objectId': '177_385900460001',
        'srcObject': 2,
        'regionKey': 177,
        'objectType': '002002002000',
        'objectCn': '77:05:0007007:4926',
        'objectCon': '77-77-09/088/2012-638',
        'subjectId': 145000000000,
        'regionId': 145296000000,
        'settlementId': 145296595000,
        'street': 'КРАСНОГО МАЯКА|УЛ',
        'house': '22|2|',
        'addressNotes': 'г.Москва, ул.Красного Маяка, д.22, корп.2, кв.187',
        'okato': None,
        'apartment': '187',
        'nobjectCn': '77:5:7007:4926',
        'nobjectCon': '77-77-9/88/2012-638'
    }
]
OBJECTS_BY_ADDRESS_RESPONSE = json.dumps(OBJECTS_BY_ADDRESS).encode('utf-8')


OBJECT_BY_ID = {
    'objectId': '177_385900460001',
    'type': 'premises',
    'regionKey': 177,
    'source': 2,
    'firActualDate': '2016-12-09',
    'objectData':
        {
            'id': '177_385900460001',
            'regionKey': 177,
            'srcObject': 2,
            'objectType': '002002002000',
            'objectName': 'квартира',
            'removed': 0,
            'dateLoad': '2015-01-11',
            'addressNote': 'г.Москва, ул.Красного Маяка, д.22, корп.2, кв.187',
            'objectCn': '77:05:0007007:4926',
            'objectCon': '77-77-09/088/2012-638',
            'objectInv': None,
            'objectUn': '77:05:0007007:4926',
            'rsCode': '77.0.6.5',
            'actualDate': '2015-01-11',
            'brkStatus': -1,
            'brkDate': None,
            'formRights': '100',
            'objectAddress': {
                'id': '177_385900460001',
                'regionKey': 177,
                'okato': '45296595000',
                'kladr': None,
                'region': '77',
                'district': None,
                'districtType': 'неопр',
                'place': None,
                'placeType': 'неопр',
                'locality': None,
                'localityType': 'неопр',
                'street': 'Красного Маяка',
                'streetType': 'ул',
                'house': '22',
                'building': '2',
                'structure': None,
                'apartment': '187',
                'addressNotes': 'г.Москва, ул.Красного Маяка, д.22, корп.2, кв.187',
                'mergedAddress': 'ул Красного Маяка, д. 22 (2), 187'
            }
        },
    'parcelData': None,
    'realtyData': None,
    'premisesData': {'id': '177_385900460001',
    'regionKey': 177,
    'premisesCn': '77:05:0007007:4926',
    'premisesCon': '77-77-09/088/2012-638',
    'premisesInv': None,
    'premisesUn': '77:05:0007007:4926',
    'literBti': None,
    'premisesType': '002002002000',
    'assignType': None,
    'premisesName': 'квартира',
    'areaValue': 76.7,
    'areaType': '060001003000',
    'areaUnit': '012002001000',
    'premisesFloor': 14,
    'premisesFloorStr': '14',
    'premisesNum': '187',
    'premisesTypeValue': None,
    'areaUnitValue': None,
    'rightsReg': True,
    'multiFlat': False,
    'premisesTypeStr': 'Помещение'},
    'rightEncumbranceObjects': [
        {'rightData': {
            'tempId': 0,
            'id': '177_337945941001',
            'objectId': '177_385900460001',
            'updatePackId': 0,
            'regionKey': 177,
            'code': '001003000000',
            'codeDesc': 'Общая совместная собственность',
            'partSize': None,
            'type': None,
            'regNum': '77-77-09/088/2012-638',
            'regDate': '2012-11-22',
            'rsCode': '77.0.6.5',
            'packageId': '7ce6c767-4ecc-4e9a-a792-136568c24d8d',
            'actualDate': '2015-01-11'},
           'encumbrances': None
        }],
 'oldNumbers': None
}
OBJECT_BY_ID_RESPONSE = json.dumps(OBJECT_BY_ID).encode('utf-8')


