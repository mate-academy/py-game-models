import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    race = None
    guild = None
    for name, info in players.items():
        if not Race.objects.filter(
            name=info["race"]["name"]
        ).exists():
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
            for skills in info["race"]["skills"]:
                Skill.objects.create(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=race
                )
        info_guild = info["guild"]
        if info_guild:
            guild_description = info_guild["description"] \
                if info_guild["description"] else None
            if not Guild.objects.filter(
                name=info["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=guild_description
                )

            guild = Guild.objects.get(
                name=info["guild"]["name"]
            )
        else:
            guild = None
        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
