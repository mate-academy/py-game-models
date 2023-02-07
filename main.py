import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        gamers = json.load(f)
        for gamer, gamer_values in gamers.items():
            if not Race.objects.filter(
                    name=gamer_values["race"]["name"]).exists():
                race_ = Race.objects.create(
                    name=gamer_values["race"]["name"],
                    description=gamer_values["race"]["description"]
                )
            else:
                race_ = Race.objects.get(name=gamer_values["race"]["name"])
            for skill in gamer_values["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_
                    )
            if gamer_values["guild"]:
                if not Guild.objects.filter(
                        name=gamer_values["guild"]["name"]).exists():
                    guild_ = Guild.objects.create(
                        name=gamer_values["guild"]["name"],
                        description=gamer_values["guild"]["description"]
                    )
                else:
                    guild_ = Guild.objects.get(
                        name=gamer_values["guild"]["name"]
                    )
            else:
                guild_ = None
            if not Player.objects.filter(nickname=gamer).exists():
                Player.objects.create(
                    nickname=gamer,
                    email=gamer_values["email"],
                    bio=gamer_values["bio"],
                    race=race_,
                    guild=guild_
                )


if __name__ == "__main__":
    main()
