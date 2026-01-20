import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_key, player_info in data.items():
        race_data = player_info.get("race")
        race_instance = None

        if isinstance(race_data, dict):
            race_name = race_data.get("name")
            race_descriptions = race_data.get("description")

            if race_name:
                race_instance, created = Race.objects.get_or_create(
                    name=race_name,
                    defaults={"description": race_descriptions}
                )
                print(created)

        skill_list = race_data.get("skills", [])

        if race_instance:
            for skill_data_dict in skill_list:
                skill_name = skill_data_dict["name"]
                skill_bonus = skill_data_dict["bonus"]

                if skill_name and skill_bonus:
                    skill, created_skill = Skill.objects.get_or_create(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=race_instance
                    )
                    print(created_skill)

        guild_instance = None
        guild_data = player_info.get("guild")

        guild_name = None
        guild_description = None

        if isinstance(guild_data, dict):
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
        elif isinstance(guild_data, str):
            guild_name = guild_data
            guild_description = None

        if guild_name:
            guild_instance, created_guild = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
            print(created_guild)

        player_actual_nickname = player_info.get("nickname", player_key)

        if not player_actual_nickname:
            print("Error, nickname not found {player_key}.")
            continue

        player, created_player = Player.objects.get_or_create(
            nickname=player_actual_nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race_instance,
                "guild": guild_instance,
            }
        )
        print(created_player)


if __name__ == "__main__":
    main()
