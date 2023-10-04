from json import load
from typing import Type, Any

from django.db import transaction
from django.db.utils import (
    DatabaseError,
    IntegrityError
)


def load_json_data(data: str) -> dict:
    with open(data) as json_data:
        return load(json_data)


def model_attrs(model: Type, data: dict[str: Any],
                rest_keys: str = "") -> dict:
    fields = dict.fromkeys(
        field.name for field in model._meta.fields
        if field.name != 'id'
        and field.name not in rest_keys.split()
    )
    for key, value in data.items():
        if key in fields:
            fields[key] = value
    return fields


def create_model_item(model: Type, item_data: dict[str: Any]) -> None:
    try:
        with transaction.atomic():
            model.objects.create(**item_data)
    except (IntegrityError, DatabaseError):
        pass
