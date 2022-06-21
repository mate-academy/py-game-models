import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json', 'r') as json_input:
        players = json.load(json_input)
    guilds = {}
    # Guild Creation
    for guild in players:
        player_dict = players[guild]
        if player_dict["guild"]:
            if player_dict["guild"]["description"]:
                description = player_dict["guild"]["description"]
            else:
                description = None
            name = player_dict["guild"]["name"]
            if Guild.objects.filter(name=name).exists() is False:
                creation = \
                    Guild.objects.create(name=name, description=description)
                guilds[name] = creation.id
    races = {}
    # Race creation
    for race in players:
        player_dict = players[race]
        name = player_dict["race"]["name"]
        description = player_dict["race"]["description"]
        if Race.objects.filter(name=name).exists() is False:
            creation = Race.objects.create(name=name, description=description)
            races[name] = creation.id
    # Skills creation
    for skill in players:
        player_dict = players[skill]
        skills = player_dict["race"]["skills"]
        race_name = player_dict["race"]["name"]
        for single_skill in skills:
            skill_name = single_skill["name"]
            bonus = single_skill["bonus"]
            if Skill.objects.filter(name=skill_name).exists() is False:
                Skill.objects.create(name=skill_name,
                                     bonus=bonus, race_id=races[race_name])
    # Players creation
    for player in players:
        player_dict = players[player]
        nickname = player
        email = player_dict["email"]
        bio = player_dict["bio"]
        race_name = player_dict["race"]["name"]
        race = races[race_name]
        if player_dict["guild"]:
            guild_name = player_dict["guild"]["name"]
            guild = guilds[guild_name]
        else:
            guild = None
        Player.objects.create(nickname=nickname, email=email,
                              bio=bio, race_id=race, guild_id=guild)


if __name__ == "__main__":
    main()
