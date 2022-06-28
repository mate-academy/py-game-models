import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_guild(guild):
    if guild:
        if not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )


def create_race(race_name: str, race_description: str):
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(
            name=race_name,
            description=race_description
        )


def create_skills(skills: dict, race):
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race)
            )


def create_player(
        nickname: str,
        email: str,
        bio: str,
        race: str,
        guild_name: str = None
):
    if not Player.objects.filter(nickname=nickname).exists():
        if guild_name:
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=Race.objects.get(name=race),
                guild=Guild.objects.get(name=guild_name)
            )
        else:
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=Race.objects.get(name=race)
            )


def main():
    with open("players.json", "r") as data:
        players = json.load(data)

    for player, value in players.items():
        email = value["email"]
        bio = value["bio"]

        create_guild(value["guild"])

        create_race(
            value["race"]["name"],
            value["race"]["description"]
        )

        create_skills(
            value["race"]["skills"],
            value["race"]["name"]
        )

        if players[player]["guild"]:
            create_player(
                player,
                email,
                bio,
                value["race"]["name"],
                value["guild"]["name"]
            )
        else:
            create_player(
                player,
                email,
                bio,
                value["race"]["name"]
            )


if __name__ == "__main__":
    main()
