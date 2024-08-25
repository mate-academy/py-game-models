import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    races_list = []
    for user in players_info:
        if players_info[user]["race"] not in races_list:
            races_list.append(players_info[user]["race"])

    for race in races_list:
        new_race = Race.objects.create(
            name=race["name"],
            description=race["description"]
        )
        for skill in race["skills"]:
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race
            )

    guilds_list = []
    for user in players_info:
        if players_info[user]["guild"] not in guilds_list:
            guilds_list.append(players_info[user]["guild"])

    for guild in guilds_list:
        if guild:
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

    for player in players_info:
        race = Race.objects.get(name=players_info[player]["race"]["name"])
        guild = Guild.objects.get(
            name=players_info[player]["guild"]["name"]
        ) if players_info[player]["guild"] else None
        Player.objects.create(
            nickname=player,
            email=players_info[player]["email"],
            bio=players_info[player]["bio"],
            race=race,
            guild=guild
        )
