import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for player in players_data:
        race_data = player.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", ""),
            defaults={"description": race_data.get("description", "")}
        )

        guild_data = player.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", ""),
                defaults={"description": guild_data.get("description", "")}
            )

        player_obj, _ = Player.objects.get_or_create(
            nickname=player.get("nickname", ""),
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )

        for skill_data in player.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data.get("name", ""),
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race
                }
            )

if __name__ == "__main__":
    main()
