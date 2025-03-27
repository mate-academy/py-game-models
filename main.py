import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as f:
        player_data = json.load(f)

    for name, player in player_data.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )
        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )

        guild, _ = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            defaults={
                "description": player["guild"]["description"]
            }
        ) if player["guild"] else (None, False)

        Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
