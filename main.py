import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description")
        )

        for skill_data in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                bonus=skill_data["bonus"]
            )

        guild = None
        if player_info["guild"]:
            guild_data = player_info["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
