import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players_data = json.load(players)
    for player_name in players_data:
        if not Race.objects.filter(
                name=players_data[player_name]["race"]["name"]
        ).exists():
            Race.objects.create(
                name=players_data[player_name]["race"]["name"],
                description=players_data[player_name]["race"]["description"]
            )
        for skill in players_data[player_name]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=Race.objects.get(
                        name=players_data[player_name]["race"]["name"]
                    ).id)
        guild = None
        if players_data[player_name]["guild"]:
            guild_info = players_data[player_name]["guild"]
            if not Guild.objects.filter(
                    name=guild_info["name"]
            ).exists():
                Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            guild = Guild.objects.get(
                name=players_data[player_name]["guild"]["name"]
            ).id
        Player.objects.create(
            nickname=player_name,
            email=players_data[player_name]["email"],
            bio=players_data[player_name]["bio"],
            race_id=Race.objects.get(
                name=players_data[player_name]["race"]["name"]
            ).id,
            guild_id=guild
        )


if __name__ == "__main__":
    main()
