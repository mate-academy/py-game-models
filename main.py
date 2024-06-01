import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player_name, player_data in players_data.items():
        race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )[0]
        guild = Guild.objects.get_or_create(
            name=player_data["guild"]["name"],
            description=player_data["guild"]["description"]
        )[0] if player_data["guild"] is not None else None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )
        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(
                    name=player_data["race"]["name"]
                )
            ) if skill is not None else None


if __name__ == "__main__":
    main()
