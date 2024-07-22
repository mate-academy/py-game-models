import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_json_file = json.load(players_file)

    for player, values in players_json_file.items():
        race, _ = Race.objects.get_or_create(
            name=values["race"]["name"],
            description=values["race"]["description"]
        )

        guild = None
        if "guild" in values and values["guild"] is not None:
            if "description" in values["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=values["guild"]["name"],
                    defaults={"description": values["guild"]["description"]}
                )

        Player.objects.get_or_create(
            nickname=player,
            email=values["email"],
            bio=values["bio"],
            race=race,
            guild=guild,
        )
        for skill in values["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )


if __name__ == "__main__":
    main()
