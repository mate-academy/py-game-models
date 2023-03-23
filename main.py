import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        is_race_exist = Race.objects.filter(
            name=players[player]["race"]["name"]
        ).exists()

        is_guild_exist = Guild.objects.filter(
            name=players[player]["guild"]["name"]
        ).exists() if players[player]["guild"] else True

        is_player_exist = Player.objects.filter(
            nickname=player
        ).exists()

        if not is_race_exist:
            Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]
            )
        if not is_guild_exist:
            Guild.objects.create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )
        for skill in players[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=players[player]["race"]["name"]
                    )
                )
        if not is_player_exist:
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(
                    name=players[player]["race"]["name"]
                ),
                guild=Guild.objects.get(
                    name=players[player]["guild"]["name"]
                ) if players[player]["guild"] else None
            )


if __name__ == "__main__":
    main()
