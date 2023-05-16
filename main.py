import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)
    for player in players:
        guild = players[player].get("guild")
        guild_instance = None
        if guild is not None:
            guild_instance = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )[0]
        race = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"]
        )[0]
        skills = players[player]["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        player_info = players[player]
        Player.objects.get_or_create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild_instance
            if guild is not None else None
        )


if __name__ == "__main__":
    main()
