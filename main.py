import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for player_name, player_info in players_data.items():
        email = player_info["email"]
        bio = player_info["bio"]

        race_name = player_info["race"]["name"]
        race_description = player_info["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        guild_info = player_info["guild"]
        if guild_info:
            guild_name = guild_info["name"]
            guild_description = guild_info["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
        else:
            guild = None

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild)

        skills_data = player_info["race"]["skills"]
        for skill_data in skills_data:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]

            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )


if __name__ == "__main__":
    main()
