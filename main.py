import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for nickname, player_data in data.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={
                    "description": player_data["race"].get("description")
                }
            )
            if player_data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description": player_data["guild"].get("description")
                    }
                )
            else:
                guild = None
            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": race
                    }
                )
            player, _ = Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                }
            )

    print(f"Total amount of players: {Player.objects.count()}")
    print(f"Total amount of skills: {Skill.objects.count()}")
    print(f"Total amount of races: {Race.objects.count()}")
    print(f"Total amount of guilds: {Guild.objects.count()}")


if __name__ == "__main__":
    main()
