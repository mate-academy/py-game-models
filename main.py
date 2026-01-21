import json
from db.models import Race, Skill, Guild, Player
from django.db import transaction


@transaction.atomic
def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    races = {}
    guilds = {}

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data["guild"]

        race_name = race_data["name"]
        if race_name not in races:
            races[race_name] = Race.objects.create(
                name=race_name,
                description=race_data.get("description", "")
            )

            for skill_data in race_data.get("skills", []):
                Skill.objects.create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=races[race_name]
                )

        guild_name = None
        if guild_data:
            guild_name = guild_data["name"]
            if guild_name not in guilds:
                guilds[guild_name] = Guild.objects.create(
                    name=guild_name,
                    description=guild_data.get("description", "")
                )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=races[race_name],
            guild=guilds.get(guild_name)
        )


if __name__ == "__main__":
    main()
