import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for key, item in players_data.items():

        if not Race.objects.filter(name=item["race"]["name"]).exists():
            Race.objects.create(
                name=item["race"]["name"],
                description=item["race"]["description"]
            )

        for skill in item["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=item["race"]["name"])
                )

        if item["guild"] is not None \
                and not Guild.objects.filter(
                name=item["guild"]["name"]).exists():
            Guild.objects.create(
                name=item["guild"]["name"],
                description=item["guild"]["description"]
            )

        Player.objects.create(
            nickname=key,
            email=item["email"],
            bio=item["bio"],
            race=Race.objects.get(name=item["race"]["name"]),
            guild=Guild.objects.get(name=item["guild"]["name"])
            if item.get("guild") else None
        )


if __name__ == "__main__":
    main()
