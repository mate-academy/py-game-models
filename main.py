import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json
from django.utils.timezone import now


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race_data = player["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skills in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                defaults={
                    "bonus": skills["bonus"],
                    "race": race
                },
            )

        guild = None
        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description": player["guild"].get("description")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
                "created_at": now()
            }
        )


if __name__ == "__main__":
    main()
