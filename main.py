import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_data in players.items():
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description")
        )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = player_data["guild"]
        guild = None
        if guild_data:
            guild, _create = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]

            )

        Player.objects.get_or_create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
