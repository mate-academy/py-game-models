import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json', 'r') as f:
        data = json.load(f)
    for player in data:
        player_list = [i[0] for i in
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
        race_list = [i[0] for i in list(Race.objects.values_list("name"))]
        if race_name in race_list:
            race = Race.objects.get(name=f"{race_name}")
        else:
            race = Race.objects.create(
                name=race_name,
                description=race_description)
        for skill in race_skills:
            ls = [i[0] for i in list(Skill.objects.values_list("name"))]
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if skill_name in ls:
                pass
            else:
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race)
        guild = player["guild"]
        try:
            guild_name = guild["name"]
        except TypeError:
            pass
        else:
            guild_description = guild["description"]
            guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description)
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
