import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_info in data.items():
        race_info = player_info.get("race")
        race, created = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info["description"]},
        )
        for skill in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race},
            )

        guild_info = player_info.get("guild")
        guild = None
        if guild_info:
            guild, created = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get["description"]},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
