import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        player["nickname"] = nickname
        print(f"Player structure: {player}")

        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"].get("description", "")}
        )

        for skill in player["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill.get("bonus", ""),
                    "race": race
                }
            )

        guild_name = player.get("guild")["name"] \
            if player.get("guild") and isinstance(player.get("guild"), dict) \
            else None
        if guild_name:
            guild_description = player["guild"].get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description or ""}
            )
        else:
            guild = None

        # Создаем игрока
        Player.objects.get_or_create(
            nickname=player["nickname"],
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
