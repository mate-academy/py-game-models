import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for name, player in players.items():
        guild = None
        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description": player["guild"]["description"],
                }
            )

        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={
                "description": player["race"]["description"],
            }
        )

        if player["race"]["skills"]:
            for skill_name in player["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_name["name"],
                    defaults={
                        "bonus": skill_name["bonus"],
                        "race": race,
                    }
                )

        player, _ = Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
