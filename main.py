import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as users_data:
        json_data = json.load(users_data)
    for user_name, user_data in json_data.items():
        race, created = Race.objects.get_or_create(
            name=user_data["race"]["name"],
            description=user_data["race"]["description"]
        )

        user_skills_data = user_data["race"]["skills"]
        for skill in user_skills_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if user_data["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=user_data["guild"]["name"],
                description=user_data["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=user_name,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
