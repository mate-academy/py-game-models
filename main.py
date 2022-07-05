import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def create_race(player):
    race_name = player["race"]["name"]
    if not Race.objects.filter(
            name=race_name
    ).exists():
        Race.objects.create(
            name=race_name,
            description=player["race"]["description"]
        )
    return Race.objects.get(
        name=race_name
    )


def create_skill(skill, player):
    if not Skill.objects.filter(
        name=skill["name"]
    ).exists():
        Skill.objects.create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=create_race(player)
        )


def create_guild(player):
    if player["guild"]:
        guild_name = player["guild"]["name"]
        if not Guild.objects.filter(
                name=guild_name
        ).exists():
            Guild.objects.create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )
        return Guild.objects.get(
            name=guild_name
        )
    return None


def main():
    with open("players.json", "r") as read_file:
        players_data = json.load(read_file)

    for player in players_data:
        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=create_race(players_data[player]),
            guild=create_guild(players_data[player])
        )
        for skill in players_data[player]["race"]["skills"]:
            create_skill(skill, players_data[player])


if __name__ == "__main__":
    main()
