import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:
        pdata = players[player]
        race, _ = Race.objects.get_or_create(
            name=pdata["race"]["name"],
            description=pdata["race"]["description"],
        )

        if pdata.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=pdata["guild"]["name"],
                description=pdata["guild"]["description"],
            )
        else:
            guild = None

        for skill_data in pdata["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )

        Player.objects.get_or_create(
            nickname=player,
            email=pdata["email"],
            bio=pdata["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
