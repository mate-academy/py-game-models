from db.models import Race, Guild


def get_player_data(players: dict) -> list:
    player_data = []
    all_data = []
    for player in players:
        nickname = player
        player_data.append(nickname)
        email = players[player]["email"]
        player_data.append(email)
        bio = players[player]["bio"]
        player_data.append(bio)
        race = Race.objects.get(name=players[player]["race"]["name"])
        player_data.append(race)
        if players[player]["guild"]:
            if players[player]["guild"]["name"]:
                guild = Guild.objects.get(
                    name=players[player]["guild"]["name"]
                )
                player_data.append(guild)
        else:
            guild = None
            player_data.append(guild)
        all_data.append(player_data)
        player_data = []
    return all_data
