import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        with open("players.json", "r") as file:
            players_data = json.load(file)
    except FileNotFoundError:
        raise Exception("File not found!")

    for player_name, player_data in players_data.items():

        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )
        guild, created = (
            Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"],
            )
            if player_data["guild"]
            else (None, True)
        )

        if player_data["race"]["skills"]:
            for skill in player_data["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill.get("name"), bonus=skill.get("bonus"), race=race
                )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
