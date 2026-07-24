import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, data in players.items():
        email = data["email"]
        bio = data["bio"]
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )
        for skill_date in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_date["name"],
                defaults={
                    "bonus": skill_date["bonus"],
                    "race": race,
                }
            )
        guild_data = data.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
        else:
            guild = None
        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
