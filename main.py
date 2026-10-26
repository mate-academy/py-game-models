import json

import init_django_orm  # noqa: F401
from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)
    for player_name, data in players_data.items():
        guild = None
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]},
        )
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )
        skills_data = race_data["skills"]
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )
        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
