import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for nickname, player in players.items():

        race_data = player.get("race")
        race_name = race_data.get("name")
        description = race_data.get("description")
        race, created = Race.objects.get_or_create(name=race_name,
                                                   description=description)

        guild = None
        guild_data = player.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        skills = race_data.get("skills")
        for skill in skills:
            name, bonus = skill["name"], skill["bonus"]

            Skill.objects.get_or_create(name=name, bonus=bonus, race=race)

        Player.objects.get_or_create(nickname=nickname,
                                     email=player["email"], guild=guild,
                                     bio=player["bio"], race=race)


if __name__ == "__main__":
    main()
