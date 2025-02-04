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
                    name=values.get("guild", {}).get("name"),
                    description=values.get("guild", {}).get("description")
                )
            else:
                guild = None
            Player.objects.create(
                nickname=nickname,
                email=values.get("email"),
                bio=values.get("bio"),
                race=race,
                guild=guild
            )
            for skill in values.get("race", {}).get("skills", []):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
