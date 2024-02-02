import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"],
        )

        if info["race"].get("skills"):
            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        guild = None
        if info.get("guild"):
            guild, _ = Guild.objects.get_or_create(**info["guild"])

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
