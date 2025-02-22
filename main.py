import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for name, player in players_data.items():
        guild = None
        if player["guild"] is not None:
            guild = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"])[0]
        race = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"])[0]

        for skill_data in player["race"]["skills"]:
            Skill.objects.get_or_create(
                race=race,
                name=skill_data["name"],
                bonus=skill_data["bonus"])

        Player.objects.create(nickname=name,
                              email=player["email"],
                              bio=player["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
