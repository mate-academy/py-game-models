import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_name, player_data in players.items():
        race = player_data["race"]
        guild = player_data["guild"]
        skills = race["skills"]

        race_name = race["name"]
        race_description = race["description"]
        race_obj = Race.object.get_or_create(
            name=race_name,
            description=race_description
        )

        for skill in skills:
            if skill:
                skill_name = skill["name"]
                skill_bonus = None
                if not Skill.objects.filter(name=skill_name).exists():
                    Skill.objects.create(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=race_obj
                    )

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
