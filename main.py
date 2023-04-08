import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data:
        player_data = json.load(data)

    for player, data in player_data.items():
        race = data["race"]
        skills = race["skills"]
        guild = data["guild"]

        if not Race.objects.filter(name=race["name"]).exists():
            race = Race.objects.create(
                name=race["name"],
                description=race["description"],
            )
        else:
            race = Race.objects.get(name=race["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild.get("description"),
                )
            else:
                guild = Guild.objects.get(name=guild["name"])

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
