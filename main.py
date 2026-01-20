import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={
                "description": player_data["race"].get("description", "")
            },
        )
        if player_data["race"]["skills"]:
            for skill_data in player_data["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]}
                )

        guild = None
        if player_data.get("guild") and player_data["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={
                    "description": player_data["guild"].get("description")
                }
            )
        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )
        if created:
            print(f"Player created: {player.nickname}")
        else:
            print(f"Player {player.nickname} already exists")


if __name__ == "__main__":
    main()
