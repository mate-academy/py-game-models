import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def race(player_info):
    race_name = player_info["race"]["name"]
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(
            name=race_name,
            description=player_info["race"]["description"]
        )
    return Race.objects.get(name=race_name)


def guild(player_info):
    if player_info["guild"]:
        guild_name = player_info["guild"]["name"]
        if not Guild.objects.filter(name=guild_name).exists():
            Guild.objects.create(**player_info["guild"])
        return Guild.objects.get(name=guild_name)
    return None


def skills(player_info, skill):
    if not Skill.objects.filter(name=skill["name"]).exists():
        Skill.objects.create(**skill, race=race(player_info))


def main():
    with open("players.json") as data_file:
        players_data = json.load(data_file)

    for player in players_data:
        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=race(players_data[player]),
            guild=guild(players_data[player]),
        )

        for skill in players_data[player]["race"]["skills"]:
            skills(players_data[player], skill)


if __name__ == "__main__":
    main()
