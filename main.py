import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    data = {}
    with open("players.json", "r") as source:
        data = json.load(source)
    for key, value in data.items():
        race_data = value["race"]
        guild_data = value["guild"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None
        for skill_item in race_data["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_item["name"],
                bonus=skill_item["bonus"],
                race=race
            )
        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race = race,
            guild = guild
        )




if __name__ == "__main__":
    main()
