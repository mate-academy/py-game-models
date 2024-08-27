import init_django_orm  # noqa: F401

from django.db import IntegrityError
import json

from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("db/tests/players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        try:
            Player.objects.create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )
        except IntegrityError:
            print(f"Player with nickname {nickname} already exists.")


if __name__ == "__main__":
    main()
