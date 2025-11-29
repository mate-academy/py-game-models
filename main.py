import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player, data in players.items():

        race = Race.objects.get_or_create(
            name=data.get("race", {}).get("name"),
            description=data.get("race", {}).get("description"))

        skills = []
        for skill in data.get("race", {}).get("skills"):
            set_skill = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race[0])
            skills.append(set_skill)

        guild = (None, None)
        if data.get("guild"):
            guild = Guild.objects.get_or_create(
                name=data["guild"].get("name"),
                description=data["guild"].get("description"))

        Player.objects.get_or_create(
            nickname=player,
            email=data.get("email"),
            bio=data.get("bio"),
            guild=guild[0],
            race=race[0])


if __name__ == "__main__":
    main()
