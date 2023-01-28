import init_django_orm  # noqa: F401
from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        players_dict = load(file)

    for player_name, info in players_dict.items():

        race_info = info["race"]

        if not Race.objects.filter(
                name=race_info["name"]
        ).exists():
            Race.objects.create(
                name=race_info["name"],
                description=race_info["description"],
            )

        for item in race_info["skills"]:
            if not Skill.objects.filter(name=item["name"]).exists():
                Skill.objects.create(
                    name=item["name"],
                    bonus=item["bonus"],
                    race=Race.objects.get(name=race_info["name"])
                )

        guild_info = info["guild"]

        if guild_info and \
                not Guild.objects.filter(name=guild_info["name"]).exists():
            Guild.objects.create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        guild_type = (
            Guild.objects.get(name=guild_info["name"])
            if guild_info else None
        )

        Player.objects.create(
            nickname=player_name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=race_info["name"]),
            guild=guild_type
        )


if __name__ == "__main__":
    main()
