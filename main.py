import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_file:
        data = json.load(data_file)

    for player in data:
        player_data = data[player]
        race = player_data["race"]
        skills = race["skills"]
        guild = player_data["guild"]

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race["name"])
                )

        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=player_data["email"],
                bio=player_data["bio"],
                race=Race.objects.get(name=race["name"]),
                guild=Guild.objects.get(name=guild["name"]) if guild else None,
            )


if __name__ == "__main__":
    main()
