import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as datafile:
        players = json.load(datafile)

    for nickname, player in players.items():
        race = player["race"]

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

        race_id = Race.objects.get(name=race["name"])

        skills = race["skills"]

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_id
                )

        guild = player["guild"]

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )

            guild_id = Guild.objects.get(name=guild["name"])
        else:
            guild_id = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=player["email"],
                bio=player["bio"],
                race=race_id,
                guild=guild_id
            )


if __name__ == "__main__":
    main()
