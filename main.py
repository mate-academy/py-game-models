import init_django_orm  # noqa: F401
from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        players_dict = load(file)

    for player_name, info in players_dict.items():
        if not Race.objects.filter(
                name=info["race"]["name"]
        ).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"],
            )

        if info["guild"] and \
                not Guild.objects.filter(name=info["guild"]["name"]).exists():
            Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        for item in info["race"]["skills"]:
            if not Skill.objects.filter(name=item["name"]).exists():
                Skill.objects.create(
                    name=item["name"],
                    bonus=item["bonus"],
                    race=Race.objects.get(name=info["race"]["name"])
                )

        guild_type = (
            Guild.objects.get(name=info["guild"]["name"])
            if info["guild"] else None
        )

        Player.objects.create(
            nickname=player_name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=info["race"]["name"]),
            guild=guild_type
        )


if __name__ == "__main__":
    main()
