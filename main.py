import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json', 'r') as player_data_file:
        data = json.load(player_data_file)
    for player in data:
        player_list = [player_[0] for player_ in
                       list(Player.objects.values_list("nickname"))]
        if player in player_list:
            continue
        nickname = player
        player = data[f"{player}"]
        email = player["email"]
        bio = player["bio"]
        race = player["race"]
        race_name = race["name"]
        race_description = race["description"]
        race_skills = race["skills"]
        race_list = [race_[0] for race_ in
                     list(Race.objects.values_list("name"))]
        if race_name in race_list:
            race = Race.objects.get(name=f"{race_name}")
        else:
            race = Race.objects.create(
                name=race_name,
                description=race_description)
        for skill in race_skills:
            skill_list = [skill_[0] for skill_ in
                          list(Skill.objects.values_list("name"))]
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if skill_name not in skill_list:
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race)
        guild = player["guild"]
        try:
            guild_name = guild["name"]
            guild_description = guild["description"]
            guild_list = [guild_[0] for guild_ in
                          list(Guild.objects.values_list("name"))]
            if guild_name in guild_list:
                guild = Guild.objects.get(name=guild_name)
            else:
                guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description)
        except TypeError:
            guild = None
        finally:
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
