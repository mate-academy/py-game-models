import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

def main():
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    race_cache = {}
    skill_cache = {}
    guild_cache = {}

    for player_name, player_data in players_data.items():
        if isinstance(player_data.get("race"), dict):
            race_name = player_data["race"]["name"]
            race_description = player_data["race"].get("description", "")

            if race_name not in race_cache:
                race, _ = Race.objects.get_or_create(name=race_name, defaults={"description": race_description})
                race_cache[race_name] = race
            else:
                race = race_cache[race_name]

            for skill_data in player_data["race"].get("skills", []):
                skill_name = skill_data["name"]
                skill_bonus = skill_data.get("bonus", "")

                if skill_name not in skill_cache:
                    skill, _ = Skill.objects.get_or_create(
                        name=skill_name,
                        defaults={"bonus": skill_bonus, "race": race}
                    )
                    skill_cache[skill_name] = skill

        guild_data = player_data.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")
            if guild_name:
                if guild_name not in guild_cache:
                    guild_description = guild_data.get("description", "")
                    guild, _ = Guild.objects.get_or_create(
                        name=guild_name,
                        defaults={"description": guild_description}
                    )
                    guild_cache[guild_name] = guild
                else:
                    guild = guild_cache[guild_name]
            else:
                guild = None
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
