import init_django_orm  # noqa: F401

from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = load(players_file)

    for player, info in players.items():
        race_name, race_description, skills = info["race"].values()

        player_race, created = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        player_guild, created = Guild.objects.get_or_create(
            name=info["guild"]["name"],
            description=info["guild"]["description"]
        ) if info["guild"] else (None, False)

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
