import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player in data.keys():
        race, _ = Race.objects.get_or_create(
            name=data[player]["race"]["name"],
            description=data[player]["race"]["description"])

        guild = None
        if data[player].get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data[player]["guild"]["name"],
                description=data[player]["guild"]["description"]
            )

        Player.objects.get_or_create(nickname=player,
                                     email=data[player]["email"],
                                     bio=data[player]["bio"],
                                     race=race,
                                     guild=guild)

        for skill in data[player]["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)


if __name__ == "__main__":
    main()
