import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as current_file:
        players_info = json.load(current_file)

    for player, value in players_info.items():
        race_temp = None
        if value["race"]:
            race_temp, _ = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
            for skill in value["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_temp
                )
        guild = None
        if value["guild"] and value["guild"]["name"]:
            guild, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=value["email"],
            bio=value["bio"],
            race=race_temp,
            guild=guild
        )


if __name__ == "__main__":
    main()
