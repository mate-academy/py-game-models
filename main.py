import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for key, value in players.items():
        race = value["race"]
        if not Race.objects.filter(name=(race["name"])).exists():
            race_obj = Race.objects.create(name=race["name"],
                                           description=race["description"])
        else:
            race_obj = Race.objects.get(name=(race["name"]))
        skills = race["skills"]
        for skill in skills:
            skill_obj = Skill.objects.filter(name=skill["name"])
            if not skill_obj:
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race_obj)
        guild = value["guild"]
        if guild:
            guild_desc = guild["description"] if guild["description"] else None
            if not Guild.objects.filter(name=guild["name"]).exists():
                guild_obj = Guild.objects.create(name=guild["name"],
                                                 description=guild_desc)
            else:
                guild_obj = Guild.objects.get(name=guild["name"])
        else:
            guild_obj = None
        Player.objects.create(nickname=key,
                              email=value["email"],
                              bio=value["bio"],
                              race=race_obj,
                              guild=guild_obj)


if __name__ == "__main__":
    main()
