import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_data = json.load(file)

    for player in player_data:
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"].get("description", "")}
        )
    for skill_data in player["race"]["skills"]:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race
        )

    guild = None
    if "guild" in player and player["guild"]:
        guild, _ = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            defaults={"description": player["guild"].get("description", None)}
        )

    Player.objects.create(
        nickname=player["nickname"],
        email=player["email"],
        bio=player["bio"],
        race=race,
        guild=guild
    )


if __name__ == "__main__":
    main()
