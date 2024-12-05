import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)
    for player_name, player_data in players_data.items():
        race_data = player_data.get("race")
        race = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )
        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"), bonus=skill.get("bonus"), race=race[0]
            )
        guild = player_data.get("guild")
        if guild:
            guild = Guild.objects.get_or_create(
                name=guild.get("name"), description=guild.get("description")
            )
            guild = guild[0]
        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race[0],
            guild=guild,
        )


if __name__ == "__main__":
    main()
