import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name in data:
        player_data = data[player_name]
        race_data = player_data["race"]
        race_name = race_data["name"]
        skills_data = race_data["skills"]
        guild_data = player_data["guild"]
        guild_name = guild_data["name"] if guild_data else None

        Race.objects.get_or_create(
            name=race_name,
            description=race_data["description"]
        )

        if skills_data:
            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_name)
                )

        if guild_data:
            Guild.objects.get_or_create(
                name=guild_name,
                description=guild_data["description"]
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=race_name),
            guild=Guild.objects.get(name=guild_name) if guild_name else None
        )


if __name__ == "__main__":
    main()
