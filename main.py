import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as f:
        players = json.load(f)

        for player, info in players.items():
            Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            for i, skill in enumerate(info["race"]["skills"]):
                race = Race.objects.get(name=info["race"]["name"])
                Skill.objects.get_or_create(
                    name=info["race"]["skills"][i]["name"],
                    bonus=info["race"]["skills"][i]["bonus"],
                    race=race
                )

            race = Race.objects.get(name=info["race"]["name"])
            if info["guild"]:
                Guild.objects.get_or_create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
                guild = Guild.objects.get(name=info["guild"]["name"])

            else:
                guild = None

            Player.objects.get_or_create(
                nickname=player,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
