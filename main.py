import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player in data:
        player_data = data[player]
        race_data = player_data["race"]
        player_race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )[0]

        skills_data = race_data["skills"]
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )

        player_guild = Guild.objects.get_or_create(
            name=player_data["guild"]["name"],
            description=player_data["guild"]["description"]
        )[0] if player_data["guild"] else None

        Player.objects.get_or_create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
