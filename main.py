import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_json:
        players = json.load(player_json)
        for player_name, player_data in players.items():
            race, created = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"],
            )

            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )
            guild = None

            if player_data["guild"] is not None:
                guild = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"],
                )

            Player.objects.create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild[0] if guild else None,
            )


if __name__ == "__main__":
    main()
