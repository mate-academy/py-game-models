import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, details in players.items():
        # Create or get Race
        race, _ = Race.objects.get_or_create(
            name=details["race"]["name"],
            defaults={"description": details["race"]["description"]}
        )

        # Create or get Guild
        guild = None
        if details.get("guild") and details["guild"].get("name"):
            guild, _ = Guild.objects.get_or_create(
                name=details["guild"]["name"],
                defaults={"description": details["guild"].get("description")}
            )

        # Create Player
        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": details["email"],
                "bio": details["bio"],
                "race": race,
                "guild": guild,
            },
        )

        # Create Skills
        for skill_data in details["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )


if __name__ == "__main__":
    main()
