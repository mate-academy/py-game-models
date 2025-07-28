import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    Player.objects.all().delete()
    Skill.objects.all().delete()
    Race.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json", "r") as input_file:
        players = json.load(input_file)

    for player in players:
        race, _ = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            defaults={
                "description": players[player]["race"]["description"]
            }
        )

        for skill_item in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_item["name"],
                defaults={
                    "bonus": skill_item["bonus"],
                    "race": race
                }
            )

        if players[player]["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                defaults={
                    "description": players[player]["guild"]["description"]
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": players[player]["email"],
                "bio": players[player]["bio"],
                "guild": guild,
                "race": race
            }
        )


if __name__ == "__main__":
    main()
