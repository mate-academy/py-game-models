import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(player_race):
    name = player_race["name"]
    description = player_race["description"]
    if not Race.objects.filter(name=name).exists():
        Race.objects.create(name=name, description=description)
    return Race.objects.get(name=name)


def create_skills(player_skills, race):
    for skill in player_skills:
        name = skill["name"]
        bonus = skill["bonus"]
        if not Skill.objects.filter(name=name).exists():
            Skill.objects.create(name=name, bonus=bonus, race=race)


def create_guild(player_guild):
    if player_guild:
        name = player_guild["name"]
        description = player_guild["description"]
        if not Guild.objects.filter(name=name).exists():
            Guild.objects.create(name=name, description=description)
        return Guild.objects.get(name=name)
    return None


def create_player(
        nickname,
        email,
        bio,
        race,
        guild
):
    if not Player.objects.filter(nickname=nickname).exists():
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


def main():
    with open("players.json", "r") as file_in:
        players_data = json.load(file_in)

        for player in players_data:
            nickname = player
            email = players_data[player]["email"]
            bio = players_data[player]["bio"]

            race = create_race(players_data[player]["race"])
            create_skills(players_data[player]["race"]["skills"], race)
            guild = create_guild(players_data[player]["guild"])

            create_player(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
