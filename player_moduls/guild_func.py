from db.models import Guild


def guild_func(player: dict):
    guild = player.get("guild")
    if guild is not None:
        if not Guild.objects.filter(name=player["guild"]["name"]).exists():
            guild_inst, created = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"]["description"]}
            )

        else:
            guild_inst = None

        return guild_inst
