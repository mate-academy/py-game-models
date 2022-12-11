import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Guild.objects.all().delete()
    Player.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    with open("players.json", "r") as file:
        players = json.load(file)
    for key, value in players.items():
        race = value["race"]
        try:
            race_obj = Race.objects.get(name=(race["name"]))
        except Exception:
            race_obj = Race.objects.create(name=race["name"],
                                           description=race["description"])
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
            try:
                guild_obj = Guild.objects.get(name=guild["name"])
            except Exception:
                guild_obj = Guild.objects.create(name=guild["name"],
                                                 description=guild_desc)
        else:
            guild_obj = None
        Player.objects.create(nickname=key,
                              email=value["email"],
                              bio=value["bio"],
                              race=race_obj,
                              guild=guild_obj)


if __name__ == "__main__":
    main()
