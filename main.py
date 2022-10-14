import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player, info in players_data.items():
        email = info["email"]
        bio = info["bio"]
        races = info["race"]
        skills = races["skills"]
        guilds = info["guild"]

        if not Race.objects.filter(name=races["name"]).exists():
            Race.objects.create(
                name=races["name"],
                description=races["description"],
            )
        race = Race.objects.get(name=races["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        if guilds:
            if not Guild.objects.filter(name=guilds["name"]).exists():
                Guild.objects.create(
                    name=guilds["name"],
                    description=guilds["description"]
                )
            guild = Guild.objects.get(name=guilds["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
