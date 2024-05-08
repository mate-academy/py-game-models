import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)
    for player_name, player_info in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )
        guild = None
        if player_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"],
            )
        for skill in player_info["race"]["skills"]:
            if skill:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
