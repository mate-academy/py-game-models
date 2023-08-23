import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for player in data:
            if Player.objects.filter(nickname=player).exists():
                continue
            guild = data[player]["guild"]
            race_dict = data[player]["race"]
            if guild is not None:
                guild = Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"],
                )[0]
            race = Race.objects.get_or_create(
                name=race_dict["name"],
                description=race_dict["description"],
            )[0]
            for skill in race_dict["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
