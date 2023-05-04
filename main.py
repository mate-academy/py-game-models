import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        player_guild = player_data["guild"]
        player_race = player_data["race"]
        player_skills = player_data["race"]["skills"]

        if player_guild:
            if not Guild.objects.filter(name=player_guild["name"]).exists():
                if player_guild["description"]:
                    guild_description = player_guild["description"]
                else:
                    guild_description = None
                Guild.objects.create(
                    name=player_guild["name"],
                    description=guild_description
                )
            guild = Guild.objects.get(name=player_guild["name"])
        else:
            guild = None

        if not Race.objects.filter(name=player_race["name"]).exists():
            if player_race["description"]:
                race_description = player_race["description"]
            else:
                race_description = ""
            Race.objects.create(
                name=player_race["name"],
                description=race_description
            )

        for skill in player_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=player_race["name"])
                )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=player_race["name"]),
            guild=guild
        )


if __name__ == "__main__":
    main()
