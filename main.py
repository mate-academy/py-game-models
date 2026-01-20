import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, player in players.items():

        race, created = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"],
        )

        if created:
            for skill in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        if player["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
