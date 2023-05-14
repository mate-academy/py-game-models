import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_info = json.load(file)

    for player_name, player_info in players_info.items():
        race_info = player_info["race"]
        skills_info = race_info["skills"]
        guild_info = player_info["guild"]

        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"],
        )

        for skill in skills_info:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
