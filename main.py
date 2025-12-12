import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


PLAYERS_FILE_NAME = "players.json"


def main() -> None:
    with open(PLAYERS_FILE_NAME, "r") as file:
        players = json.load(file)
    for name, data in players.items():

        race_data = data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        guild = None
        if data.get("guild", False):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"].get("name"),
                description=data["guild"].get("description")
            )

        if race_data.get("skills", False):
            for skill in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        Player.objects.create(
            nickname=name,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
