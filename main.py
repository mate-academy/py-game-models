import init_django_orm  # noqa: F401

from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = load(players_file)

    for player, info in players.items():
        race_name, race_description, skills = info["race"].values()

        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        player_race = Race.objects.get(name=race_name)

        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=player_race
                    )

        if info["guild"] and not (
                Guild.objects.filter(name=info["guild"]["name"]).exists()
        ):
            Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        player_guild = Guild.objects.get(
            name=info["guild"]["name"]
        ) if info["guild"] else None

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
