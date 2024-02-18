from data_from_players.get_guild_data import get_guild_data

from db.models import Guild
from players_json import players_data


def create_guild() -> Guild:
    guild_data = get_guild_data(players_data)
    for guild in guild_data:
        print(guild, guild_data[guild])
        Guild.objects.get_or_create(
            name=guild,
            description=guild_data[guild],
        )
    return Guild.objects
