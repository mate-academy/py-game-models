import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as f:
        data_file = json.load(f)
    for user, user_info in data_file.items():
        race_obj, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"]
        )   # Add new Race object in DB.
        for skill in user_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )  # Add new Skills object in DB.
        guild = None
        if user_info["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=user_info["guild"]["name"],
                description=user_info["guild"]["description"]
            )  # Add new Guild object in DB.

        Player.objects.get_or_create(
            nickname=user,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race_obj,
            guild=guild,
        )


if __name__ == "__main__":
    main()
