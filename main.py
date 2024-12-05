import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, info in players.items():
        is_race_exist = Race.objects.filter(
            name=info["race"]["name"]
        ).exists()

        is_guild_exist = Guild.objects.filter(
            name=info["guild"]["name"]
        ).exists() if info["guild"] else True

        is_player_exist = Player.objects.filter(
            nickname=player
        ).exists()

        if not is_race_exist:
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        if not is_guild_exist:
            Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        players_race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=players_race
                )

        players_guild = Guild.objects.get(
            name=info["guild"]["name"]
        ) if info["guild"] else None

        if not is_player_exist:
            Player.objects.create(
                nickname=player,
                email=info["email"],
                bio=info["bio"],
                race=players_race,
                guild=players_guild
            )


if __name__ == "__main__":
    main()
