import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

def main() -> None:
    with open("players.json", "r") as f:
        player_data = json.load(f)

    for player_name, player in player_data.items():
        race_data = player["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        guild_obj = None
        if player.get("guild"):
            guild_data = player["guild"]
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        player_obj, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race_obj,
            guild=guild_obj
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race_obj,
                defaults={
                    "bonus": skill["bonus"],
                }
            )

if __name__ == "__main__":
    main()
