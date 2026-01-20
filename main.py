import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)

    for nickname, info in players_dict.items():
        cur_race, _ = (Race.objects.get_or_create
                       (name=info["race"]["name"],
                        description=info["race"]["description"]))

        if info["race"]["skills"]:
            for skill in info["race"]["skills"]:
                cur_skill, _ = (Skill.objects.get_or_create
                                (name=skill["name"],
                                 bonus=skill["bonus"],
                                 race=cur_race))

        cur_guild = None
        if info.get("guild"):
            cur_guild, _ = (Guild.objects.get_or_create
                            (name=info["guild"]["name"],
                             description=info["guild"]["description"]))

        Player.objects.create(nickname=nickname,
                              email=info["email"],
                              bio=info["bio"],
                              race=cur_race,
                              guild=cur_guild)


if __name__ == "__main__":
    main()
