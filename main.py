import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name, info in data.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            defaults={"description": info["race"]["description"]}
        )

        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        guild_data = info.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
