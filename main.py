import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, data in players_data.items():
        race_data = data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
            print(f"Skill: {skill.name}, Created: {created}")

        guild_data = data.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
