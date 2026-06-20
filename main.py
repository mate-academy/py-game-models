import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        guild_obj = None
        if player_data["guild"] is not None:
            if Guild.objects.filter(name=player_data["guild"]["name"]).exists():
                guild_obj = Guild.objects.get(name=player_data["guild"]["name"])
            else:
                guild_obj = Guild.objects.create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"])

        if Race.objects.filter(name=player_data["race"]["name"]).exists():
            race_obj = Race.objects.get(name=player_data["race"]["name"])
        else:
            race_obj = Race.objects.create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"])

        for skill in player_data["race"]["skills"]:
            if Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.get(name=skill["name"])
            else:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
