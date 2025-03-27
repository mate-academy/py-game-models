import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"],
        )

        if created:
            if skills := info["race"].get("skills"):
                for skill in skills:
                    Skill.objects.get_or_create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race
                    )

        if guild := info.get("guild"):
            guild, _ = Guild.objects.get_or_create(**guild)

        Player.objects.create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
