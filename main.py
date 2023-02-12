import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players_info = json.load(players)

    for player_name, player_data in players_info.items():

        guild = player_data["guild"] if player_data["guild"] else None
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )
        players_guild = (
            Guild.objects.get(name=guild["name"]) if guild else None
        )

        race = player_data["race"]
        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

        skills = race["skills"]
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race["name"])
                )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=race["name"]),
            guild=players_guild
        )


if __name__ == "__main__":
    main()
