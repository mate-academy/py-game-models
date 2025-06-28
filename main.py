import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for nick, player in players.items():
            guild = player.get("guild")
            race, _ = Race.objects.get_or_create(
                name=player["race"]["name"],
                description=player["race"]["description"],
            )
            for skill_ in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_["name"],
                    bonus=skill_["bonus"],
                    race=race,
                )
            if guild is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"],
                )
            if guild is None:
                guild = None
            Player.objects.get_or_create(
                nickname=nick,
                email=player["email"],
                bio=player["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
