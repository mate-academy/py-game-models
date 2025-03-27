import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        user = players_data[player_data]
        skills = players_data.get(player_data).get("race").get("skills")

        Race.objects.get_or_create(
            name=user.get("race").get("name"),
            description=user.get("race").get("description")
        )
        race_id = Race.objects.get(name=user.get("race").get("name"))

        if user.get("guild"):
            Guild.objects.get_or_create(
                name=user.get("guild").get("name"),
                description=user.get("guild").get("description")
            )
            guild = Guild.objects.get(name=user.get("guild").get("name"))
        else:
            guild = None

        if skills:
            for one_skill in skills:
                Skill.objects.get_or_create(
                    name=one_skill.get("name"),
                    bonus=one_skill.get("bonus"),
                    race=race_id
                )

        Player.objects.get_or_create(
            nickname=player_data,
            email=user.get("email"),
            bio=user.get("bio"),
            race=race_id,
            guild=guild
        )


if __name__ == "__main__":
    main()
