import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        info_for_players = json.load(file)
    for name in info_for_players:
        Race.objects.get_or_create(
            name=info_for_players.get(name).get("race")["name"],
            description=info_for_players.get(name).get("race")["description"]
        )
        for skill in info_for_players.get(name).get("race").get("skills"):
            race = Race.objects.get(
                name=info_for_players.get(name).get("race").get("name")
            )
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race)
        if info_for_players.get(name).get("guild") is not None:
            Guild.objects.get_or_create(
                name=info_for_players.get(name).get("guild").get("name"),
                description=(
                    info_for_players.get(name).get("guild").get("description")
                )
            )
        Player.objects.create(
            nickname=name,
            email=info_for_players.get(name).get("email"),
            bio=info_for_players.get(name).get("bio"),
            race=Race.objects.get(
                name=info_for_players.get(name).get("race").get("name")
            ),
            guild=(
                Guild.objects.get(
                    name=info_for_players.get(name).get("guild").get("name")
                )
                if info_for_players.get(name).get("guild") is not None
                else None
            )




        )


if __name__ == "__main__":
    main()
