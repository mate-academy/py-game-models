import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as f:
        players_info = json.load(f)
    for pl in players_info.keys():
        race, created = Race.objects.get_or_create(
            name=players_info[pl]["race"]["name"],
            description=players_info[pl]["race"]["description"]
        )
        if created and players_info[pl]["race"]["skills"]:
            for skill in players_info[pl]["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        guild = None
        if players_info[pl]["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=players_info[pl]["guild"]["name"],
                description=players_info[pl]["guild"]["description"]
            )

        Player.objects.create(
            nickname=pl,
            email=players_info[pl]["email"],
            bio=players_info[pl]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
