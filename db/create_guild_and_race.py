from db.models import Race, Guild


def create_race_and_guild(users_data):
    for nickname, other_data in users_data.items():

        race_data = other_data["race"]
        guild_data = other_data["guild"]

        race_already_exists = Race.objects.filter(
            name=race_data["name"],
            description=race_data["description"]
        )

        if not race_already_exists:
            Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )

        if guild_data:
            guild_already_exists = Guild.objects.filter(
                name=guild_data["name"],
                description=guild_data["description"]
            )

            if not guild_already_exists:
                Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
