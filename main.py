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

        race, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild.get("description"),
            )

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
