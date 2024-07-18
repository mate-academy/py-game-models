import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as f:
        player_data = json.load(f)

    for player_name, player_info in player_data.items():
        email = player_info["email"]
        bio = player_info["bio"]

        race_data = player_info["race"]
        race, created_race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        print(Race.objects.all())

        skills = []
        for skill_data in race_data.get("skills", []):
            skill, created_skill = Skill.objects.get_or_create(
                name=skill_data["name"], race=race, bonus=skill_data["bonus"]
            )
            skills.append(skill)
        print(Skill.objects.all())

        guild_data = player_info.get("guild")
        guild = None
        if guild_data:
            guild, created_guild = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        print(Guild.objects.all())

        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
        )

        print(Player.objects.all())


if __name__ == "__main__":
    main()
