import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_players:
        data_players = json.load(file_players)
    for player_name, player in data_players.items():
        data = player.get("guild")
        if data:
            guild, _ = Guild.objects.get_or_create(
                name=data["name"],
                description=data["description"]
            )
        else:
            guild = None
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )
        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"]},
                race=race
            )
        Player.objects.create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
