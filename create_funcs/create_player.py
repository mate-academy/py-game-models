from datetime import datetime

from db.models import Player, Race, Guild, Skill


def create_player(players: dict) -> Player:
    for player in players:
        nickname = player
        email = players[player]["email"]
        bio = players[player]["bio"]
        race_name = players[player]["race"]["name"]
        race_description = players[player]["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description,
        )
        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race_name)
            )
        if players[player]["guild"]:
            guild_name = players[player]["guild"]["name"]
            guild_description = players[player]["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description if guild_description else None
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=Race.objects.get(name=race_name),
            guild=guild,
            created_at=datetime.now(),
        )
    return Player.objects
