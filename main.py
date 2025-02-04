import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
        for nickname, values in players.items():
            race, create_race = Race.objects.get_or_create(
                name=values["race"]["name"],
                description=(
                    values["race"]["description"]
                    if values["race"]["description"]
                    else ...
                )
            )
            if values["guild"]:
                guild, create_guild = Guild.objects.get_or_create(
                    name=values["guild"]["name"],
                    description=(
                        values["guild"]["description"]
                        if values["guild"]["description"]
                        else None
                    )
                )
            else:
                guild = None
            Player.objects.create(
                nickname=nickname,
                email=values["email"],
                bio=values["bio"],
                race=race,
                guild=guild
            )
            if isinstance(values["race"]["skills"], list):
                if values["race"]["skills"]:
                    for skill in values["race"]["skills"]:
                        Skill.objects.get_or_create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=race
                        )


if __name__ == "__main__":
    main()
