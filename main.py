import json

import init_django_orm  # noqa: F401
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

        race_instance, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill in player_race["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            skill_instance, created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race_instance}
            )

        guild_instance = None
        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            guild_instance, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": player_data["guild"]["description"]}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
