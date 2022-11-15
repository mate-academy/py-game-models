import init_django_orm  # noqa: F401

from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players = load(data_file)
    for user_name, user_inform in players.items():
        player_race = user_inform["race"]
        if not Race.objects.filter(
            name=player_race["name"]
        ).exists():
            Race.objects.create(name=player_race["name"],
                                description=player_race["description"])

        player_guild = user_inform["guild"]
        if player_guild is not None and not Guild.objects.filter(
            name=player_guild["name"]
        ).exists():
            Guild.objects.create(
                name=player_guild["name"],
                description=player_guild["description"]
            )

        player_skill = user_inform["race"]["skills"]
        for skill in player_skill:
            if not Skill.objects.filter(
                name=skill["name"]
            ).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=player_race["name"])
                )

        try:
            Player.objects.create(
                nickname=user_name,
                email=user_inform["email"],
                bio=user_inform["bio"],
                race=Race.objects.get(name=player_race["name"]),
                guild=Guild.objects.get(name=player_guild["name"])
            )
        except TypeError:
            Player.objects.create(
                nickname=user_name,
                email=user_inform["email"],
                bio=user_inform["bio"],
                race=Race.objects.get(name=player_race["name"])
            )


if __name__ == "__main__":
    main()
