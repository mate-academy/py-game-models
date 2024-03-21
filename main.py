import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as f:
        data_file = json.load(f)
    for user, user_info in data_file.items():
        race_obj = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"]
        )   # Add new Race object in DB.
        for skill in user_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj[0]
            )  # Add new Skills object in DB.
        player = Player.objects.get_or_create(
            nickname=user,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race_obj[0],
        )
        if user_info["guild"] is not None:
            guild_obj = Guild.objects.get_or_create(
                name=user_info["guild"]["name"],
                description=user_info["guild"]["description"]
            )   # Add new Guild object in DB.
            player[0].guild = guild_obj[0]
            player[0].save()  # Save the update in to DB.


if __name__ == "__main__":
    main()
