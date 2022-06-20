import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def add_race(race_data):
    name = race_data.get("name")
    if not Race.objects.filter(name=name).exists():
        description = race_data.get("description")
        Race.objects.create(name=name, description=description)
    return Race.objects.get(name=name)


def add_skills(skill_data, race):
    for skill in skill_data:
        name = skill.get("name")
        if not Skill.objects.filter(name=name).exists():
            bonus = skill.get("bonus")
            Skill.objects.create(name=name, bonus=bonus, race=race)


def add_guild(guild_data):
    if guild_data:
        name = guild_data.get("name")
        if not Guild.objects.filter(name=name).exists():
            description = guild_data.get("description")
            Guild.objects.create(name=name, description=description)
        return Guild.objects.get(name=name)
    return None


def add_player(player_data, nickname):
    if not Player.objects.filter(nickname=nickname):
        email = player_data.get("email")
        bio = player_data.get("bio")
        race = add_race(player_data.get("race"))
        add_skills(player_data.get("race").get("skills"), race=race)
        guild = add_guild(player_data.get("guild"))
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild)


def main():
    with open('players.json', 'r') as players_data:
        pd = json.load(players_data)

    for player in pd:
        add_player(player_data=pd[player], nickname=player)

    print(Player.objects.all())


if __name__ == "__main__":
    main()
