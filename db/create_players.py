from db.models import Player, Race, Guild


def create_players(users_data: dict) -> list:

    players = {}

    for nickname, other_data in users_data.items():
        race_data = other_data["race"]
        race = Race.objects.get(
            name=race_data["name"]
        )
        guild_data = other_data["guild"]
        if guild_data:
            guild_data = Guild.objects.get(
                name=guild_data["name"]
            )

        Player.objects.create(
            nickname=nickname,
            email=other_data["email"],
            bio=other_data["bio"],
            race=race,
            guild=guild_data,
        )

    return list(players.values())

