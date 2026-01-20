import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)
    for key, value in players.items():
        race = None
        race_data = value.get("race")
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data.get("description", "")
            )

        guild = None
        guild_data = value.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )

        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value.get("bio", ""),
            race=race,
            guild=guild
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
