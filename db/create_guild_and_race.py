from db.models import Race, Guild


def create_race_and_guild(users_data: dict) -> tuple:

    races = {}
    guilds = {}

    for nickname, other_data in users_data.items():

        race_data = other_data["race"]
        guild_data = other_data["guild"]

        race = Race(
            name=race_data["name"],
            description=race_data["description"]
        )

        races[race.name] = race

        if guild_data:

            guild = Guild(
                name=guild_data["name"],
                description=guild_data["description"]
            )

            guilds[guild.name] = guild

    return list(races.values()), list(guilds.values())
