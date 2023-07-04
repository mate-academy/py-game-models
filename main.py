import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)

    for player, player_info in players_info.items():
        guild = player_info["guild"] if player_info["guild"] else None
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        race = player_info["race"]
        racing, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        skills = race["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=racing
            )

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=racing,
            guild=guild
        )


if __name__ == "__main__":
    main()
