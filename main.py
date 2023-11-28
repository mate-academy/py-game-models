import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Player.objects.all().delete()
    file_name = "players.json"
    with open(file_name) as f:
        players_dict = json.load(f)

    for name, value_player in players_dict.items():
        race_, bool_ = Race.objects.get_or_create(
            name=value_player["race"]["name"],
            description=value_player["race"]["description"]
        )

        if not value_player["guild"]:
            guild_ = None
        else:
            guild_, bool_ = Guild.objects.get_or_create(
                name=value_player["guild"]["name"],
                description=value_player["guild"]["description"]
            )

        for skill in value_player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_
            )

        Player.objects.create(
            nickname=name,
            email=value_player["email"],
            bio=value_player["bio"],
            race=race_,
            guild=guild_
        )


if __name__ == "__main__":
    main()
