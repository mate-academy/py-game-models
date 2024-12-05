import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for user_name in data:
        user = data[user_name]
        race, _ = Race.objects.get_or_create(
            name=user["race"]["name"],
            description=user["race"]["description"])

        for skill_data in user["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"], race=race
            )

        guild = None
        if user.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=user["guild"]["name"],
                description=user["guild"]["description"])

        Player.objects.get_or_create(
            nickname=user_name,
            email=user["email"],
            bio=user["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
