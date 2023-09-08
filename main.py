import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_dictionary = json.load(players_file)

    for player_name, player_data in players_dictionary.items():
        player_email = player_data["email"]
        player_bio = player_data["bio"]

        player_race = player_data["race"]
        race_name = player_race["name"]
        race_description = player_race["description"]

        if not Race.objects.filter(name=race_name).exists():
            race_instance = Race.objects.create(
                name=race_name,
                description=race_description
            )
        else:
            race_instance = Race.objects.get(name=race_name)

        for skill in player_race["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_instance
                )

        guild_instance = None
        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            if not Guild.objects.filter(name=guild_name).exists():
                guild_description = player_data["guild"]["description"]
                guild_instance = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            else:
                guild_instance = Guild.objects.get(name=guild_name)

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
