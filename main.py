import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        skills = data["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild_data = data["guild"]
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
