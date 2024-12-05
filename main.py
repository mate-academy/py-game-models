import json


import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as players_file:
        data = json.load(players_file)

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        race_name = race_data["name"]
        race_description = race_data["description"]
        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description},
        )

        for skill_data in race_data["skills"]:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            Skill.objects.get_or_create(name=skill_name,
                                        race=race,
                                        bonus=skill_bonus)

        guild = None
        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            guild_description = player_data["guild"]["description"]
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description},
            )

        Player.objects.update_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
