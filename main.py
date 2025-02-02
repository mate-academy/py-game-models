import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    guild_cache = {}
    race_cache = {}
    skill_cache = {}

    for player in data:
        race_name = player["race"]["name"]
        race_description = player["race"]["description"]

        if race_name not in race_cache:
            race_obj = Race.objects.create(
                name=race_name,
                description=race_description
            )
            race_cache[race_name] = race_obj
        else:
            race_obj = race_cache[race_name]

        for skill in player["race"]["skills"]:
            skill_name = skill["name"]
            if skill_name not in skill_cache:
                skill_obj = Skill.objects.create(
                    name=skill_name,
                    bonus=skill["bonus"],
                    race=race_obj
                )
                skill_cache[skill_name] = skill_obj

        guild_data = player.get("guild")
        guild_obj = None
        if guild_data:
            guild_name = guild_data["name"]
            if guild_name not in guild_cache:
                guild_obj = Guild.objects.create(
                    name=guild_name,
                    description=guild_data["description"]
                )
                guild_cache[guild_name] = guild_obj
            else:
                guild_obj = guild_cache[guild_name]

        Player.objects.create(
            nickname=player["nickname"],
            email=player["email"],
            bio=player["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
