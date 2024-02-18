from datetime import datetime

from db.models import Player, Race, Guild


def create_player(players: dict) -> Player:
    guild = None
    for player in players:
        nickname = player
        email = players[player]["email"]
        bio = players[player]["bio"]
        race = Race.objects.get(name=players[player]["race"]["name"])
        if players[player]["guild"]:
            if players[player]["guild"]["name"]:
                guild = Guild.objects.get(
                    name=players[player]["guild"]["name"]
                )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
            created_at=datetime.now(),
        )
    return Player.objects
