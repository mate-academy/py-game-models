import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        user = players_data[player_data]
        skills = players_data[player_data]["race"]["skills"]

        Race.objects.get_or_create(
            name=user["race"]["name"],
            description=user["race"]["description"]
        )
        race_id = Race.objects.get(name=user["race"]["name"])

        if user["guild"]:
            Guild.objects.get_or_create(
                name=user["guild"]["name"],
                description=user["guild"]["description"]
            )
            guild = Guild.objects.get(name=user["guild"]["name"])
        else:
            guild = None

        if skills:
            for one_skill in skills:
                Skill.objects.get_or_create(
                    name=one_skill["name"],
                    bonus=one_skill["bonus"],
                    race=race_id
                )

        Player.objects.get_or_create(
            nickname=player_data,
            email=user["email"],
            bio=user["bio"],
            race=race_id,
            guild=guild
        )


if __name__ == "__main__":
    main()
