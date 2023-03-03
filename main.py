import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    dict_of_race = {}
    dict_of_guild = {}
    for player_name in data:
        race_data = data[player_name]["race"]["name"]
        description_of_race = data[player_name]["race"]["description"] \
            if data[player_name]["race"]["description"] else None
        dict_of_race[race_data] = description_of_race
        if data[player_name]["guild"] is not None:
            guild_data = data[player_name]["guild"]["name"]
            description_of_guild = data[player_name]["guild"]["description"] \
                if data[player_name]["guild"]["description"] else None
            dict_of_guild[guild_data] = description_of_guild
    for name_of_race, description in dict_of_race.items():
        if not Race.objects.filter(name=name_of_race).exists():
            Race.objects.create(name=name_of_race, description=description)
    for name_of_guild, description in dict_of_guild.items():
        if not Guild.objects.filter(name=name_of_guild).exists():
            Guild.objects.create(name=name_of_guild, description=description)

    for player_name in data:
        race_id = Race.objects.get(name=data[player_name]["race"]["name"]).id
        guild_data = data[player_name]["guild"]["name"]\
            if data[player_name]["guild"] else None
        guild_id = Guild.objects.get(name=guild_data).id\
            if data[player_name]["guild"] else None
        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(nickname=player_name,
                                  email=data[player_name]["email"],
                                  bio=data[player_name]["bio"],
                                  race_id=race_id,
                                  guild_id=guild_id,
                                  )
        for skill in data[player_name]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race_id
                )


if __name__ == "__main__":
    main()
