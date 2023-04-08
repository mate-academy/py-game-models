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
            player_race = Race.objects.create(
                name=race["name"],
                description=race["description"],
            )
        else:
            player_race = Race.objects.get(name=race["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race,
                )

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                player_guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild.get("description"),
                )
            else:
                player_guild = Guild.objects.get(name=guild["name"])
        else:
            player_guild = None

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=player_race,
            guild=player_guild,
        )


if __name__ == "__main__":
    main()
