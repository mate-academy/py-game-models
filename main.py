import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        email = data["email"]
        bio = data["bio"]

        guild_data = data.get("guild")
        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )

        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_item in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_item["name"],
                race=race,
                defaults={
                    "bonus": skill_item["bonus"],
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
