import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as f:
        lines = json.load(f)
        for player in lines:
            race, created = Race.objects.get_or_create(
                name=lines[player]["race"]["name"],
                description=lines[player]["race"]["description"])
            for skill_name in lines[player]["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_name["name"],
                    bonus=skill_name["bonus"], race=race)
            if lines[player]["guild"] is not None:
                guild, created = Guild.objects.get_or_create(
                    name=lines[player]["guild"]["name"],
                    description=lines[player]["guild"]["description"])
            else:
                guild = None

            player, created = Player.objects.get_or_create(
                nickname=player,
                email=lines[player]["email"],
                bio=lines[player]["bio"],
                race=race,
                guild=guild)


if __name__ == "__main__":
    main()
