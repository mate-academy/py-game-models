import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as f:
        information = json.load(f)
        for nickname, information in information.items():
            race, created = Race.objects.get_or_create(
                name=information["race"]["name"],
                description=information["race"]["description"])
            for skill_name in information["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_name["name"],
                    bonus=skill_name["bonus"], race=race)

            if information["guild"] is not None:
                guild, created = Guild.objects.get_or_create(
                    name=information["guild"]["name"],
                    description=information["guild"]["description"])
            else:
                guild = None

            player, created = Player.objects.get_or_create(
                nickname=nickname,
                email=information["email"],
                bio=information["bio"],
                race=race,
                guild=guild)


if __name__ == "__main__":
    main()
