import json
import init_django_orm  #noqa:f401
from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players = json.load(f)

    for nickname, player_data in players.items():
        race_info = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")}
        )

        for skill in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )

        guild = None
        guild_info = player_data.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
