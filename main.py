import init_django_orm  # noqa: F401
import json
from pathlib import Path
from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_path = Path(__file__).parent / "players.json"
    with open(players_path, "r") as f:
        players_data = json.load(f)

    for nickname, player_info in players_data.items():

        race_obj, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"].get("description")}
        )

        guild_obj = None
        if player_info.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={"description": player_info["guild"].get(
                    "description")}
            )

        player_obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )

        if not created:
            player_obj.email = player_info["email"]
            player_obj.bio = player_info["bio"]
            player_obj.race = race_obj
            player_obj.guild = guild_obj
            player_obj.save()

        for skill_data in player_info["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race_obj,
                defaults={"bonus": skill_data["bonus"]}
            )


if __name__ == "__main__":
    main()
