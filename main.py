import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


import json


def main() -> None:
    races = {}
    guild = {}

    with open("players.json", "r") as file:
        date = json.load(file)

    for players_name, players_data in date.items():
        date_for_race = players_data["race"]
        date_for_guild = players_data["guild"]

        race_name = None
        if date_for_race:
            race_name = date_for_race["name"]
            if race_name not in races:
                races[race_name] = Race.objects.create(
                    name=race_name,
                    description=date_for_race.get("description", "")
                )

                for skill_data in date_for_race.get("skills", []):
                    Skill.objects.create(
                        name=skill_data["name"],
                        bonus=skill_data["bonus"],
                        race=races[race_name]
                    )

        guild_name = None
        if date_for_guild:
            guild_name = date_for_guild["name"]
            if guild_name not in guild:
                guild[guild_name] = Guild.objects.create(
                    name=guild_name,
                    description=date_for_guild.get("description", "")
                )

        Player.objects.create(
            nickname=players_name,
            email=players_data["email"],
            bio=players_data["bio"],
            race=races[race_name],
            guild=guild.get(guild_name)
        )


if __name__ == "__main__":
    main()
