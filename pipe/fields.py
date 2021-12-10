from typing import List
from .utils import find_by


def serialize_fields(source: dict, fields: List[dict], custom: dict) -> dict:
    result = {}
    custom = custom or {}

    for key in source:
        try:
            field = find_by('key', key, fields)

            if (field):
                field_key = field['key']
                field_name = custom.get(field_key)
                field_value = serialize_field_value(
                    serialize_field_type(field, source[key])
                )

                if (field_name):
                    result[field_name] = field_value
                else:
                    result[field_key] = field_value
        except Exception as err:
            print(f"*** Error: {err}\n")
            pass

    return result


FIELD_TEXT = ['varchar', 'varchar_auto', 'text']
FIELD_FLOAT = ['double', 'monetary']
FIELD_EMAIL = ['email']
FIELD_PHONE = ['phone']
FIELD_ENUM = ['enum']


def serialize_field_value(value):
    if (type(value) == list):
        return serialize_field_value(value[0])
    elif (type(value) == dict):
        return value.get('value')
    else:
        return value


def serialize_field_type(field: dict, value: any):
    if (not value):
        return None

    if (field['field_type'] in FIELD_TEXT):
        return value
    elif (field['field_type'] in FIELD_FLOAT):
        float(value)
    elif (field['field_type'] in FIELD_ENUM):
        option = find_by('id', value, field['options'])
        if (not option):
            return None

        return option['label']
    else:
        return value
