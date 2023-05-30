from db.models import Player, Race, Guild


def create_players(users_data):
    for nickname, other_data in users_data.items():
        # Check if race exist
        race_data = other_data["race"]
        race_in_database = Race.objects.get(name=race_data["name"])
        # if race_in_database:
        #     race = race_in_database
        # else:
        #     race = Race.objects.create(
        #         name=race_data["name"],
        #         description=race_data["description"]
        #     )

        # Check if guild exist
        guild_data = other_data["guild"]
        if guild_data:
            guild_in_database = Guild.objects.get(
                name=guild_data["name"]
            )
        else:
            guild_in_database = guild_data

        Player.objects.create(
            nickname=nickname,
            email=other_data["email"],
            bio=other_data["bio"],
            race=race_in_database,  # race
            guild=guild_in_database,
        )
