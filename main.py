import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player_info in players:
        player = players[player_info]
        race_obj, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"].get("description", "")})
        guild_obj = player.get("guild")
        if guild_obj:
            guild_obj, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description":
                        player["guild"].get(
                            "description",
                            ""
                        )
                }
            )
        player_obj, _ = Player.objects.get_or_create(
            nickname=player_info,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )
        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race_obj,
                defaults={"bonus": skill.get("bonus", "")}
            )


if __name__ == "__main__":
    main()
