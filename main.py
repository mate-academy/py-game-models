import init_django_orm  # noqa: F401

from json import load

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        gamers = load(file)

    for gamer_nickname, gamer_data in gamers.items():
        races = gamer_data["race"]
        skills = races["skills"]
        guilds = gamer_data["guild"]

        if not Race.objects.filter(name=races["name"]).exists():
            Race.objects.create(
                name=races["name"],
                description=races["description"]
            ),
        race = Race.objects.get(name=races["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race

                ),
        if guilds:
            if not Guild.objects.filter(name=guilds["name"]).exists():
                Guild.objects.create(
                    name=guilds["name"],
                    description=guilds["description"]
                ),
            guild = Guild.objects.get(name=guilds["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=gamer_nickname,
            email=gamer_data["email"],
            bio=gamer_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
