import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    race = None
    for name, info in players.items():
        info_race = info["race"]
        if not Race.objects.filter(
            name=info_race["name"]
        ).exists():
            race = Race.objects.create(
                name=info_race["name"],
                description=info_race["description"]
            )
            for skills in info_race["skills"]:
                Skill.objects.create(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=race
                )
        info_guild = info["guild"]
        guild = None
        if info_guild is not None:
            guild_description = (
                info_guild["description"] if info_guild["description"] else
                None
            )
            if not Guild.objects.filter(
                name=info_guild["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=info_guild["name"],
                    description=guild_description
                )
            guild = Guild.objects.get(
                name=info_guild["name"]
            )

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
