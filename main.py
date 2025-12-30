import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data:
        data = json.load(data)
    for player in data:
        race_ = Race.objects.get_or_create(name=data[player]["race"]["name"],
                                           description=data[player]
                                           ["race"]["description"],
                                           )[0] if data[player]["race"] \
            else None

        guild_ = Guild.objects.get_or_create(name=data[player]["guild"]
                                             ["name"],
                                             description=data[player]["guild"]
                                             ["description"],
                                             )[0] if data[player]["guild"] \
            else None

        for skill in data[player]["race"]["skills"] \
                if data[player]["race"]["skills"] \
                else []:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race_,
                                        )

        Player.objects.create(nickname=player,
                              email=data[player]["email"],
                              bio=data[player]["bio"],
                              race=race_,
                              guild=guild_,
                              )


if __name__ == "__main__":
    main()
