import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        # create guild
        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(**player["guild"])
        else:
            guild = None

        # create race
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        # create skills
        if player["race"].get("skills"):
            for skill in player["race"]["skills"]:
                Skill.objects.get_or_create(**skill, race=race)

        # create player
        Player(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        ).save()


if __name__ == "__main__":
    main()
