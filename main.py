import json
from myapp.models import Race, Skill, Guild, Player


def load_races(race_data):
    for race in race_data:
        Race.objects.get_or_create(
            name=race["name"],
            description=race.get("description", "")
        )


def load_skills(skill_data):
    for skill in skill_data:
        race = Race.objects.get(name=skill["race"])
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def load_guilds(guild_data):
    for guild in guild_data:
        Guild.objects.get_or_create(
            name=guild["name"],
            description=guild.get("description", None)
        )


def load_players(player_data):
    for player in player_data:
        race = Race.objects.get(name=player["race"])
        guild = (Guild.objects.get(name=player["guild"])
                 if player.get("guild") else None)

        Player.objects.get_or_create(
            nickname=player["nickname"],
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


def main():
    with open("players.json") as file:
        data = json.load(file)

    race_data = data.get("races", [])
    skill_data = data.get("skills", [])
    guild_data = data.get("guilds", [])
    player_data = data.get("players", [])

    load_races(race_data)
    load_skills(skill_data)
    load_guilds(guild_data)
    load_players(player_data)
