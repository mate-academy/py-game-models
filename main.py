import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        players_info = json.load(file)

    for player_name, players_data in players_info.items():
        race, _ = Race.objects.get_or_create(
            name=players_data["race"]["name"],
            description=players_data["race"]["description"]
        )

        for skill in players_data["race"]["skills"]:
            Skill.objects.get_or_create(
                race=race,
                name=skill["name"],
                bonus=skill["bonus"]
            )

        guild = players_data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=players_data["email"],
            bio=players_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
