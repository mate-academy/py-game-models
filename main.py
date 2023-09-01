import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)
    race_set = set()
    skill_set = set()
    guild_set = set()
    for name, player in players_data.items():
        rase = player["race"]
        if rase["name"] not in race_set:
            race_set.add(rase["name"])
            Race.objects.create(
                name=rase["name"],
                description=rase["description"]
            )
        rase_from_db = Race.objects.get(name=rase["name"])
        for skill in rase["skills"]:
            if skill["name"] not in skill_set:
                skill_set.add(skill["name"])
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=rase_from_db
                )

        guild = player["guild"]
        print(guild)
        if guild is not None:
            if guild["name"] not in guild_set:
                guild_set.add(guild["name"])
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            guild = Guild.objects.get(name=guild["name"])
        Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=rase_from_db,
            guild=guild
        )
