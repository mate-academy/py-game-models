import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player in players_data:
        player_data = players_data[player]
        race_data = player_data.get("race")
        skills_data = race_data.get("skills")
        guild_data = player_data["guild"]

        race_name = race_data.get("name")
        race_desc = race_data.get("description")
        race, race_created = Race.objects.get_or_create(
            name=race_name, description=race_desc
        )

        skills = []
        if skills_data:
            for skill in skills_data:
                name = skill["name"]
                bonus = skill["bonus"]
                skills.append(
                    Skill.objects.get_or_create(
                        name=name,
                        bonus=bonus,
                        race=race
                    )
                )

        if guild_data:
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data["name"], description=guild_data["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
