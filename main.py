import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={
                "description": player["race"].get("description", "")
            }
        )

        for skills in player["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skills["name"],
                race=race,
                defaults={
                    "bonus": skills["bonus"]
                }
            )

        guild = None
        if player.get("guild"):
            guild = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description": player["guild"].get("description", None)
                }
            )[0]

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
