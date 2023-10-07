import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)
    for player, player_data in players.items():
        guild = player_data.get("guild")
        guild_instance = None
        if guild is not None:
            guild_instance, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )
        skills = player_data["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        player_info = player_data
        Player.objects.get_or_create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
