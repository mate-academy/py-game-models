import json
from pathlib import Path
from db.models import Race, Skill, Guild, Player


def main() -> None:
    players_file = Path(__file__).resolve().parent / "players.json"

    with open(players_file, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    Player.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Race.objects.all().delete()

    for player in players_data:
        race_data = player.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")},
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race,
                },
            )

        guild = None
        guild_data = player.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")},
            )

        Player.objects.get_or_create(
            nickname=player.get("nickname"),
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
