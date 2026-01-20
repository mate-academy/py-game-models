import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        race_info = player.get("race", {})
        guild_info = player.get("guild")
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description")}
        )

        for skill in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill.get("bonus"), "race": race}
            )

        guild, _ = Guild.objects.get_or_create(
            name=guild_info["name"],
            defaults={"description": guild_info.get("description")}
        )

        Player.objects.get_or_create(
            nickname=player["nickname"],
            defaults={
                "email": player["email"],
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
