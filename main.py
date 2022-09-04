import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def _get_players_data():
    with open("players.json", "r") as json_file:
        players_data = json.load(json_file)
    return players_data


def _fill_unique_race_and_skill_into_table(race: dict):
    if Race.objects.filter(name=race["name"]).exists():
        return Race.objects.get(name=race["name"])

    else:
        players_race = Race(
            name=race["name"],
            description=race["description"]
        )
        players_race.save()

        for skill in race["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=players_race
                )
        return players_race


def _fill_unique_guild_into_table(guild_data: dict):
    if guild_data is None:
        return None

    if Guild.objects.filter(name=guild_data["name"]).exists():
        return Guild.objects.get(
            name=guild_data["name"],
            description=guild_data["description"]
        )
    else:
        guild = Guild(
            name=guild_data["name"],
            description=guild_data["description"]
        )
        guild.save()
        return guild


def main():
    players_data = _get_players_data()
    for player_name, player_data in players_data.items():
        player = Player(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=_fill_unique_race_and_skill_into_table(
                player_data["race"]
            )
        )
        player.guild = _fill_unique_guild_into_table(player_data["guild"])
        player.save()


if __name__ == "__main__":
    main()
