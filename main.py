import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():

        race_data = player_data["race"]
        race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )[0]

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild = None
        if player_data["guild"]:
            guild = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"].get("description")
            )[0]

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
