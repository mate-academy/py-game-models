import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for user in data:
        if data[user]["guild"]:
            guild_info = Guild.objects.get_or_create(
                name=data[user]["guild"]["name"],
                description=data[user]["guild"]["description"])[0]
        else:
            guild_info = None
        player = Player.objects.create(
            nickname=user,
            email=data[user]["email"],
            bio=data[user]["bio"],
            race=Race.objects.get_or_create(
                name=data[user]["race"]["name"],
                description=data[user]["race"]["description"]
            )[0],

            guild=guild_info
        )
        skills = data[user]["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player.race
            )


if __name__ == "__main__":
    main()
