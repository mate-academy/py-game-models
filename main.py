import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

        Race.objects.all().delete()
        Guild.objects.all().delete()
        Skill.objects.all().delete()
        Player.objects.all().delete()

        for player, data in players.items():

            race, _ = Race.objects.get_or_create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )

            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            ) if data["guild"] else (None, None)

            if data["race"]["skills"]:
                for skill in data["race"]["skills"]:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.get_or_create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=race
                        )

            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
