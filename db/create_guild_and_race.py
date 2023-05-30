from db.models import Race, Guild


def create_race_and_guild(users_data: dict) -> None:
    for nickname, other_data in users_data.items():

        race_data = other_data["race"]
        guild_data = other_data["guild"]

        Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        if guild_data:
            Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
