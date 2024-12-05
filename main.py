import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config_file:
        players_data = json.load(config_file)

    for player_name, player_data in players_data.items():

        race_data = player_data["race"]
        guild_data = player_data["guild"]
        skills_data = race_data["skills"]

        race, race_created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill_data in skills_data:
            skill, skill_created = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        if guild_data:
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
