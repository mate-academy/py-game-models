import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)
    for player_name, player in data.items():
        race_data, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"],
        )
        guild_data = None
        if player.get("guild"):
            guild_data, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"],
            )

        for skill_data in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race_data
            )
        Player.objects.get_or_create(
            nickname=player_name,
            race=race_data,
            guild=guild_data,
            email=player["email"],
            bio=player.get("bio", "")
        )


if __name__ == "__main__":
    main()
