import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player in data.items():

        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        for skill in player["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                **skill, race_id=race
            )

        guild, _ = Guild.objects.get_or_create(**player["guild"]) \
            if player["guild"] else None

        Player.objects.create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race_id=race,
            guild_id=guild
        )


if __name__ == "__main__":
    main()
