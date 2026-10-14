import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for player_data in players_data:
        race_data = player_data.pop("race")
        guild_data = player_data.pop("guild", None)

        race, _ = Race.objects.get_or_create(name=race_data)
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(name=guild_data)

        player = Player.objects.create(race=race, guild=guild, **player_data)
        print(f"Created player: {player.nickname}")

        guild = None
        if player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(name=player_data["guild"])
        
        # criar o player
        Player.objects.create(
            nickname=player_data["nickname"],
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )    
        


if __name__ == "__main__":
    main()
    