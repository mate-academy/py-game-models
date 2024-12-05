import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def analyse_skills(input_skills: dict, input_race: Race) -> None:
    """Function add new skills in DB"""
    for skill in input_skills:
        unique_name = skill["name"]
        if not Skill.objects.filter(name=unique_name):
            Skill.objects.create(
                name=unique_name, bonus=skill["bonus"], race=input_race
            )


def main() -> None:
    with open("players.json", "r") as f:
        users = json.load(f)
    for username in users:
        user_data = users[username]
        race, _ = Race.objects.get_or_create(
            name=user_data["race"]["name"],
            description=user_data["race"]["description"],
        )
        analyse_skills(user_data["race"]["skills"], race)
        if user_data["guild"] is None:
            guild = None
        else:
            guild, _ = Guild.objects.get_or_create(
                name=user_data["guild"]["name"],
                description=user_data["guild"]["description"],
            )
        Player.objects.create(
            nickname=username,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
