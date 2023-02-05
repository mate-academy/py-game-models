import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as read_file:
        players = json.load(read_file)

    for player_name, info in players.items():
        if not Race.objects.filter(
                name=info["race"]["name"]).exists():
            race, created = Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

        if info["guild"] is not None:
            if not Guild.objects.filter(
                    name=info["guild"]["name"]).exists():
                guild, created = Guild.objects.get_or_create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )

        skills = info["race"]["skills"]

        for skill in skills:
            if not Skill.objects.filter(
                    name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
