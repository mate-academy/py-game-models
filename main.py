import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)
    for name, obj in players_dict.items():
        race = obj.get("race")
        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        guild = obj.get("guild")
        try:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        except TypeError:
            guild_obj = None

        Player.objects.create(
            nickname=name,
            email=obj["email"],
            bio=obj["bio"],
            race=race_obj,
            guild=guild_obj
        )

        skills = obj["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )


if __name__ == "__main__":
    main()
