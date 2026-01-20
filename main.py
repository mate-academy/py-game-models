import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player_name, values in players.items():
        player_race, bool = Race.objects.get_or_create(
            name=values.get("race").get("name"),
            description=values.get("race").get("description"),
        )
        if values["race"].get("skills"):
            for skill in values["race"].get("skills"):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=Race.objects.get(
                        name=values["race"].get("name"),
                        description=values["race"].get("description"),
                    )
                )
        player_guild = None
        if values.get("guild"):
            player_guild, bool = Guild.objects.get_or_create(
                name=values["guild"].get("name"),
                description=values["guild"].get("description"),
            )
        obj, bool = Player.objects.get_or_create(
            nickname=player_name,
            email=values.get("email"),
            bio=values.get("bio"),
            race=player_race,
            guild=player_guild
        )
        print(obj.nickname)


if __name__ == "__main__":
    main()
