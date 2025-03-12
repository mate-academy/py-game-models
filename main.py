import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"].get("description"),
        )

        for skill_data in data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data.get("bonus"),
                race=race,
            )

        guild_data = data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(**guild_data)

        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
