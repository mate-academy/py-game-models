import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file_read:
        players = json.load(file_read)

    for player in players:
        players_data = players[player]

        #  guild
        if players_data["guild"] is not None:
            if not Guild.objects.filter(
                    name=players_data["guild"]["name"]).exists():
                Guild.objects.create(
                    name=players_data["guild"]["name"],
                    description=players_data["guild"]["description"])
                players_guild = Guild.objects.get(
                    name=players_data["guild"]["name"])
        else:
            players_guild = None

        #  race
        if not Race.objects.filter(name=players_data["race"]["name"]).exists():
            Race.objects.create(
                name=players_data["race"]["name"],
                description=players_data["race"]["description"])
        players_race = Race.objects.get(name=players_data["race"]["name"])

        # skill
        for skill in players_data["race"]["skills"]:
            skill_name = skill["name"]
            if not Skill.objects.filter(name=skill_name).exists():
                skill_bonus = skill["bonus"]
                Skill.objects.create(name=skill_name,
                                     bonus=skill_bonus,
                                     race=players_race)

        #  player
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(nickname=player,
                                  email=players_data["email"],
                                  bio=players_data["bio"],
                                  race=players_race,
                                  guild=players_guild)


if __name__ == "__main__":
    main()
