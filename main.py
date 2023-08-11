import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_data = json.load(file)

    for player_name, player_info in player_data.items():
        race_data = player_info["race"]
        guild_data = player_info["guild"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        print(race)

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        skills = []
        for skill_data in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
            skills.append(skill)

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
