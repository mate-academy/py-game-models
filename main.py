import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main():
    guild_list = []
    race_list = []
    skill_list = []

    with open("players.json") as f:
        info = json.load(f)

        for player in info:

            for player_info in info[player]:

                if player_info == "race":
                    if info[player][player_info]["name"] in race_list:
                        continue
                    race_list.append(info[player][player_info]["name"])
                    Race.objects.create(
                        name=info[player][player_info]["name"],
                        description=info[player][player_info]["description"]
                    )

                    if info[player][player_info]["skills"] == [] or \
                            info[player][player_info]["skills"] in skill_list:
                        continue
                    for skill in info[player][player_info]["skills"]:
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=Race.objects.get(
                                name=info[player][player_info]["name"]
                            )
                        )

                if player_info == "guild":
                    if info[player][player_info] is None \
                            or info[player][player_info]["name"] in guild_list:
                        continue
                    guild_list.append(info[player][player_info]["name"])
                    Guild.objects.create(
                        name=info[player][player_info]["name"],
                        description=info[player][player_info]["description"]
                    )

            if info[player]["guild"] is None:
                continue
            else:
                Player.objects.create(
                    nickname=player,
                    email=info[player]["email"],
                    bio=info[player]["bio"],
                    race=Race.objects.get(name=info[player]["race"]["name"]),
                    guild=Guild.objects.get(name=info[player]["guild"]["name"])
                )


if __name__ == "__main__":
    main()
