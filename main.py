import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_name, player_data in players.items():
        guild = player_data["guild"]

        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        for skill in player_data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race)

        if not guild:
            guild_obj = None
        else:
            guild_name = guild["name"]
            guild_description = guild["description"] \
                if guild["description"] else None
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description,
                )
            guild_obj = Guild.objects.get(name=guild_name)

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
