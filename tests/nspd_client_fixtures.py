import json


PARCEL_BY_COORDINATES = {
    'type': 'FeatureCollection',
    'features': [
        {
            'id': 107884024,
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [4186735.1563343047, 7510872.4871132625],
                        [4186759.1133232918, 7510828.219564488],
                        [4186839.2036212482, 7510680.176274887],
                        [4186840.5647401814, 7510677.526427105],
                        [4186735.1563343047, 7510872.4871132625]
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
                'cadastralDistrictsCode': 77,
                'category': 36368,
                'categoryName': 'Земельные участки ЕГРН',
                'descr': '77:01:0001044:79',
                'externalKey': '77:01:0001044:79',
                'interactionId': 107818319,
                'label': '77:01:0001044:79',
                'options': {
                    'area': None,
                    'cad_num': '77:01:0001044:79',
                    'cost_application_date': '2025-01-01',
                    'cost_approvement_date': '',
                    'cost_determination_date': '2024-01-01',
                    'cost_index': 112070.59,
                    'cost_registration_date': '2024-12-08',
                    'cost_value': 827628979.39,
                    'declared_area': 7384.89,
                    'determination_couse': 'Акт об утверждении результатов определения кадастровой стоимости, полученных в соответствии с положениями Закона 237-ФЗ',
                    'land_record_area': 7384.89,
                    'land_record_category_type': 'Земли населенных пунктов',
                    'land_record_reg_date': '2007-01-01',
                    'land_record_subtype': 'Землепользование',
                    'land_record_type': 'Земельный участок',
                    'ownership_type': None,
                    'permitted_use_established_by_document': 'эксплуатации улично-дорожной сети',
                    'previously_posted': 'Ранее учтенный',
                    'quarter_cad_number': '77:01:0001044',
                    'readable_address': 'Российская Федерация, г. Москва, вн.тер.г. муниципальный округ Тверской, ул. Тверская, з/у 2Д',
                    'specified_area': None,
                    'status': 'Ранее учтенный'
                },
                'subcategory': 5,
                'systemInfo': {
                    'inserted': '2024-02-22T13:46:07.506382',
                    'insertedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79',
                    'updated': '2026-10-21T15:18:30.189037',
                    'updatedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79'
                }
            }
        }
    ]
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
    'type': 'FeatureCollection',
    'features': [
        {
            'id': 34982758,
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [5465425.373577463, 7524467.898493769],
                        [5465425.409797057, 7524449.136005895],
                        [5465430.667759769, 7524449.131199871],
                        [5465430.458780463, 7524434.214025703],
                        [5465425.373577463, 7524467.898493769]
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
                'cadastralDistrictsCode': 16,
                'category': 36369,
                'categoryName': 'Здания',
                'descr': '16:50:110108:2815',
                'externalKey': '16:50:110108:2815',
                'interactionId': 34953462,
                'label': '16:50:110108:2815',
                'options': {
                    'build_record_area': 961.6,
                    'build_record_registration_date': '2014-01-20',
                    'build_record_type_value': 'Здание',
                    'building_name': 'Здание Республиканской юношеской библиотеки',
                    'cad_num': '16:50:110108:2815',
                    'cost_application_date': '2024-01-01',
                    'cost_approvement_date': '',
                    'cost_determination_date': '2023-01-01',
                    'cost_index': 24782.06,
                    'cost_registration_date': '2023-12-19',
                    'cost_value': 23830433.51,
                    'cultural_heritage_val': '',
                    'determination_couse': 'Акт об утверждении результатов определения кадастровой стоимости, полученных в соответствии с положениями Закона 237-ФЗ',
                    'facility_cad_number': '',
                    'floors': '2',
                    'intersected_cad_numbers': None,
                    'materials': 'Кирпичные',
                    'ownership_type': 'Государственная субъекта РФ',
                    'permitted_use_name': None,
                    'previously_posted': 'Учтенный',
                    'purpose': 'Нежилое',
                    'quarter_cad_number': '16:50:110108',
                    'readable_address': 'Российская Федерация, Республика Татарстан (Татарстан), г.о. город Казань, г Казань, пр-кт Ибрагимова, д. 53б',
                    'right_type': 'Оперативное управление;Собственность',
                    'status': 'Учтенный',
                    'underground_floors': '',
                    'united_cad_numbers': '',
                    'year_built': '1979',
                    'year_commisioning': ''
                },
                'subcategory': 1,
                'systemInfo': {
                    'inserted': '2023-02-13T07:39:22.434796',
                    'insertedBy': '00000000-0000-0000-0000-000000000001',
                    'updated': '2026-10-16T22:32:44.623383',
                    'updatedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79'
                }
            }
        }
    ]
}
BUILDING_BY_COORDINATES_RESPONSE = json.dumps(BUILDING_BY_COORDINATES).encode('utf-8')

BUILDING_BY_CADASTRAL_ID = {
    'data': {
        'type': 'FeatureCollection',
        'features': [
            {
                'id': 426068044,
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiPolygon',
                    'coordinates': [
                        [
                            [
                                [4186818.703101783, 7510723.087208178],
                                [4186818.588962701, 7510723.098658164],
                                [4186818.4792457945, 7510723.132203082],
                                [4186818.3781674206, 7510723.186553819],
                                [4186818.703101783, 7510723.087208178]
                            ]
                        ],
                        [
                            [
                                [4186639.5303060245, 7511054.878903374],
                                [4186639.350930481, 7511055.1855010465],
                                [4186645.172595911, 7511058.606023198],
                                [4186645.351971303, 7511058.299425252],
                                [4186639.5303060245, 7511054.878903374]
                            ]
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
                    'cadastralDistrictsCode': 77,
                    'category': 36383,
                    'categoryName': 'Сооружения',
                    'descr': '77:01:0001005:2106',
                    'externalKey': '77:01:0001005:2106',
                    'interactionId': 408542429,
                    'label': '77:01:0001005:2106',
                    'options': {
                        'address_readable_address': 'г. Москва, ул. Тверская',
                        'cad_number': '77:01:0001005:2106',
                        'cost_application_date': '2026-01-01',
                        'cost_approvement_date': '',
                        'cost_determination_date': '2025-01-01',
                        'cost_index': 1324.64,
                        'cost_registration_date': '2025-12-11',
                        'cost_value': 2976466.08,
                        'cultural_heritage_val': '',
                        'determination_couse': 'Акт об утверждении результатов определения кадастровой стоимости, полученных в соответствии с положениями Закона 237-ФЗ',
                        'facility_cad_number': '',
                        'object_type_value': 'Сооружение',
                        'ownership_type': 'Частная',
                        'params_area': 0,
                        'params_built_up_area': 0,
                        'params_depth': 0,
                        'params_extension': 2247,
                        'params_floors': '',
                        'params_height': 0,
                        'params_name': 'Телефонная канализация',
                        'params_occurence_depth': 0,
                        'params_purpose': 'коммунальное',
                        'params_underground_floors': '',
                        'params_volume': 0,
                        'params_year_built': '',
                        'params_year_commisioning': '1950',
                        'permitted_uses_name': None,
                        'quarter_cad_number': '77:01:0000000',
                        'registration_date': '2013-11-25',
                        'status': 'Ранее учтенный',
                        'united_cad_number': ''
                    },
                    'subcategory': 1,
                    'systemInfo': {
                        'inserted': '2024-12-09T10:40:13.886576',
                        'insertedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79',
                        'updated': '2026-09-16T21:00:06.158388',
                        'updatedBy': '7EF5CD0B-AC08-4097-AF2B-07CD85992A79'
                    }
                }
            }
        ]
    },
    'meta': [
        {
            'totalCount': 1,
            'categoryId': 36383
        }
    ]
}
BUILDING_BY_CADASTRAL_ID_RESPONSE = json.dumps(BUILDING_BY_CADASTRAL_ID).encode('utf-8')


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
