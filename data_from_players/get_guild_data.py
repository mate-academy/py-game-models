def get_guild_data(players: dict) -> dict:
    guild_data = dict()
    for player in players:
        if players[player]["guild"]:
            if (players[player]["guild"]["name"]
                    and players[player]["guild"]["description"]):
                guild_data.update(
                    {
                        players[player]["guild"]["name"]:
                            players[player]["guild"]["description"]
                    }
                )
            else:
                guild_data.update({players[player]["guild"]["name"]: None})
    return guild_data
