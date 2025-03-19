import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        with open("players.json") as f:
            data_players = json.load(f)
        print(data_players)
    except FileNotFoundError:
        data_players = {}

    for data_player in data_players.values():
        guild = None
        if data_player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data_player["guild"]["name"],
                description=data_player["guild"]["description"],
            )
        race = None
        if data_player.get("race"):
            race, _ = Race.objects.get_or_create(
                name=data_player["race"]["name"],
                description=data_player["race"]["description"],
            )

        if data_player.get("skills"):
            Skill.objects.get_or_create(
                name=data_player["name"],
                bonus=data_player["bonus"],
                race=race,
            )

        if data_player.get("nickname"):
            player, _ = Player.objects.get_or_create(
                nickname=data_player["nickname"],
                email=data_player["email"],
                bio=data_player["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
