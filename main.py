import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
        for nickname, player_data in players_data.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={
                    "description": player_data["race"]["description"]
                },
            )
            if player_data["guild"] is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description": player_data["guild"]["description"]
                    },
                )
            else:
                guild = None
            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"], race=race,
                    defaults={"bonus": skill["bonus"]})
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                },
            )


if __name__ == "__main__":
    main()
