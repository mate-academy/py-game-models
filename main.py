import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for nickname, info in players.items():
        guild = info.get("guild")
        race = info.get("race")
        skills = info["race"].get("skills")

        if guild is not None:
            if not Guild.objects.filter(name=guild["name"]).exists():
                guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            else:
                guild = Guild.objects.get(name=guild["name"])

        if not Race.objects.filter(name=race["name"]).exists():
            race = Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

            for skill in skills:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        else:
            race = Race.objects.get(name=race["name"])

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
