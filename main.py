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

        if user_inform["guild"] is not None:
            if not \
                    Guild.objects.filter(
                        name=user_inform["guild"]["name"]
                    ).exists():
                player_guild = Guild.objects.create(
                    name=user_inform["guild"]["name"],
                    description=user_inform["guild"]["description"]
                )
        else:
            player_guild = None

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

        if not Player.objects.filter(nickname=user_name).exists():
            Player.objects.create(
                nickname=user_name,
                email=user_inform["email"],
                bio=user_inform["bio"],
                race=Race.objects.get(name=player_race["name"]),
                guild=player_guild)


if __name__ == "__main__":
    main()
