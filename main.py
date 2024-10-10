import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    races = {}
    guilds = {}
    skills_to_create = []
    players_to_create = []

    for player in data:
        race_name = data[player]["race"]["name"]
        race_description = data[player]["race"]["description"]
        if race_name not in races:
            races[race_name] = Race(
                name=race_name, description=race_description)

        guild_data = data[player].get("guild")
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            if guild_name not in guilds:
                guilds[guild_name] = Guild(
                    name=guild_name, description=guild_description)

    # Save races and guilds first
    Race.objects.bulk_create(races.values(), ignore_conflicts=True)
    Guild.objects.bulk_create(guilds.values(), ignore_conflicts=True)

    # Retrieve saved objects
    saved_races = {race.name: race
                   for race in Race.objects.all()}
    saved_guilds = {guild.name: guild
                    for guild in Guild.objects.all()}

    for player in data:
        race_name = data[player]["race"]["name"]
        race = saved_races[race_name]

        for skill in data[player]["race"]["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            skills_to_create.append(Skill(
                name=skill_name, bonus=skill_bonus, race=race))

        guild_data = data[player].get("guild")
        player_guild = None
        if guild_data:
            guild_name = guild_data["name"]
            player_guild = saved_guilds[guild_name]

        player_name = player
        player_email = data[player]["email"]
        player_bio = data[player]["bio"]
        players_to_create.append(Player(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=race,
            guild=player_guild))

    # Bulk create skills and players
    Skill.objects.bulk_create(skills_to_create, ignore_conflicts=True)
    Player.objects.bulk_create(players_to_create, ignore_conflicts=True)


if __name__ == "__main__":
    main()
