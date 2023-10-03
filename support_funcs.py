from django.db import transaction
from django.db.utils import (
    DatabaseError,
    IntegrityError
)
from json import load
from typing import Type


def load_json_data(data: str) -> dict:
    with open(data) as json_data:
        return load(json_data)


def write_class_attrs(attrs_dict: dict, data: dict) -> dict:
    for data_key, data_value in data.items():
        if data_key in attrs_dict:
            attrs_dict[data_key] = data_value
    return attrs_dict


def fill_class_attrs(cls: Type,
                     data: dict,
                     rest_keys: list[str] | None = None) -> dict:
    cls_name_len = len(cls.__name__)
    attrs_string = cls.__dict__["__doc__"][cls_name_len:]
    redundant = ["(", ")", ",", "id"]
    all_redundant = redundant if not rest_keys else redundant + rest_keys
    for simbl in all_redundant:
        attrs_string = attrs_string.replace(simbl, "")
    attrs = dict.fromkeys(attrs_string.split())
    cls_params = write_class_attrs(attrs, data)
    return cls_params


def create_model_item(model: Type, item_data: dict) -> None:
    try:
        with transaction.atomic():
            model.objects.create(**item_data)
    except (IntegrityError, DatabaseError):
        pass
