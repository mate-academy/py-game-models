import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as player_info:
        players = json.load(player_info)

    for player, info in players.items():
        # create guild
        guild_data = info["guild"]
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        # create race and skills of race
        race_data = info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        skills = race_data.get("skills", [])
        for skill_data in skills:
            Skill.objects.get_or_create(
                name=skill_data.get("name", ""),
                bonus=skill_data.get("bonus", 0),
                race=race
            )
        # player create
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    main()
