import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race_data = player.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")},
        )

        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race,
                }
            )

        guild_data = player.get("guild")
        guild = None
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
