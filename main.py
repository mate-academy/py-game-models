import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = f.read()

    for player in players:
        player = eval(player)

        race = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"],
        )[0]

        guild = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            description=player["guild"]["description"],
        )[0]

        Player.objects.create(
            nickname=player["nickname"],
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )

        for skill in player["race"]["skills"]:
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,  
        )


if __name__ == "__main__":
    main()
