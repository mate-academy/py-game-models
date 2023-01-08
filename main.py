import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        dicts = json.load(file)
    for name in dicts:
        p_dict = dicts[name]
        if Race.objects.filter(name=p_dict["race"]["name"]).exists():
            race = Race.objects.get(name=p_dict["race"]["name"])
        else:
            race = Race.objects.create(name=p_dict["race"]["name"],
                                       description=p_dict["race"]
                                       ["description"]
                                       )

        for skill in p_dict["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race
                                     )

        if p_dict["guild"]:
            if Guild.objects.filter(name=p_dict["guild"]["name"]).exists():
                guild = Guild.objects.get(name=p_dict["guild"]["name"])
            else:
                guild = Guild.objects.create(name=p_dict["guild"]["name"],
                                             description=p_dict["guild"]
                                             ["description"]
                                             )
        else:
            guild = None

        Player.objects.create(nickname=name,
                              email=p_dict["email"],
                              bio=p_dict["bio"],
                              race=race,
                              guild=guild
                              )


if __name__ == "__main__":
    main()
