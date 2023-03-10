import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        race_name = players[player]["race"]["name"]
        race_description = players[player]["race"]["description"]
        new_race = Race.objects.filter(name=race_name).exists()
        if not new_race:
            Race.objects.create(name=race_name, description=race_description)

        guild_name = (players[player]["guild"]["name"]
            if players[player]["guild"] else None)
        if guild_name is not None:
            guild_description = players[player]["guild"]["description"]
            new_guild = Guild.objects.filter(name=guild_name).exists()
            if not new_guild:
                guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

        skills = players[player]["race"]["skills"]
        race = Race.objects.filter(name=race_name)[0]
        for skill in skills:
            new_skill = Skill.objects.filter(name=skill["name"]).exists()
            if not new_skill:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        email = players[player]["email"]
        bio = players[player]["bio"]
        if players[player]["guild"] is None:
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race,
            )
        else:
            guild = Guild.objects.filter(name=guild_name)[0]
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
