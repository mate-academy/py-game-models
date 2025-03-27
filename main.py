import json
from typing import Any

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def add_simple_record(
        model: Any,
        filter_field_name: str,
        **kwargs
) -> Any:
    """Returns DB record instance"""
    if not model.objects.filter(
            **{filter_field_name: kwargs[filter_field_name]}
    ).exists():
        record = model.objects.create(**kwargs)
        return record
    return model.objects.get(**{filter_field_name: kwargs[filter_field_name]})


def add_player(nickname: str, data: dict) -> None:
    race_data = data.pop("race")
    skills = race_data.pop("skills")
    data["race"] = add_simple_record(Race, "name", **race_data)
    for skill_data in skills:
        add_simple_record(Skill, "name", **skill_data, race=data["race"])
    if data["guild"]:
        data["guild"] = add_simple_record(Guild, "name", **data["guild"])
    add_simple_record(Player, "nickname", nickname=nickname, **data)


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for nickname, data in players.items():
        add_player(nickname, data)


if __name__ == "__main__":
    main()
