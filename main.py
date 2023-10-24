import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players_data = json.load(players).items()
    for name, data in players_data:
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"])

        guild, _ = Guild.objects.get_or_create(
            name=data["guild"]["name"],
            description=data["guild"]["description"]
        ) if data["guild"] else (None, True)

        if data["race"]["skills"]:
            for skill_data in data["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )

        Player.objects.get_or_create(nickname=name, email=data["email"],
                                     bio=data["bio"], race=race, guild=guild)


if __name__ == "__main__":
    main()
