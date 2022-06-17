import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def make_guild(player_guild_data):
    if player_guild_data:
        name = player_guild_data["name"]
        if not Guild.objects.filter(name=name).exists():
            description = player_guild_data["description"]
            Guild.objects.create(
                name=name,
                description=description
            )
        return Guild.objects.get(name=name)
    return None


def make_race(player_race_data):
    name = player_race_data["name"]
    if not Race.objects.filter(name=name).exists():
        description = player_race_data["description"]
        Race.objects.create(
            name=name,
            description=description
        )
    return Race.objects.get(name=name)


def make_skills(player_skills_data, race):
    for skill in player_skills_data:
        name = skill["name"]
        if not Skill.objects.filter(name=name).exists():
            bonus = skill["bonus"]
            Skill.objects.create(
                name=name,
                bonus=bonus,
                race=race
            )


def make_player(
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
        players = json.load(file_in)

    for player in players:
        nickname = player
        email = players[player]["email"]
        bio = players[player]["bio"]

        race = make_race(players[player]["race"])
        make_skills(players[player]["race"]["skills"], race)
        guild = make_guild(players[player]["guild"])
        make_player(
            nickname,
            email,
            bio,
            race,
            guild
        )


if __name__ == "__main__":
    main()
