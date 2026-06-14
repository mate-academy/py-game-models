import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race_data = player.get("race")

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data.get("description", "")
            }
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )

        guild = None
        guild_data = player.get("guild")

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description")
                }
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
