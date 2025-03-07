import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for nickname, player_data in players_data.items():
        guild = None
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description"))

        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description"))

        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name") ,
                bonus=skill.get("bonus"),
                race=race)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
