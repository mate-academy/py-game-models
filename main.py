import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]
        race_instance, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description")}
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race_instance,
                defaults={"bonus": skill["bonus"]}
            )

        guild_data = player_data.get("guild")
        guild_instance = None
        if guild_data is not None:
            guild_instance, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race_instance,
                "guild": guild_instance,
            }
        )


if __name__ == "__main__":
    main()
