import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():

        if player_data["race"].get("description") is None:
            race = Race.objects.get_or_create(
                name=player_data["race"]["name"]
            )[0]
        else:
            race = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )[0]

        if not player_data["guild"]:
            guild = None
        else:
            guild = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"].get("description")
            )[0]

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race)

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
