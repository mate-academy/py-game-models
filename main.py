import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_user_info(user_data):
    race = user_data.get("race", {}).get("name") if user_data.get("race") else None
    guild = user_data.get("guild", {}).get("name") if user_data.get("guild") else None
    skills = [skill["name"] for skill in user_data.get("race", {}).get("skills", [])] if user_data.get("race") else []
    return race, guild, skills


def main() -> None:

    with open("players.json") as file:
        data = json.load(file)

    races = set()
    guilds = set()
    skills = set()
    for username, user_data in data.items():
        race, guild, skill = get_user_info(user_data)

        if race:
            races.add(race)
        if guild:
            guilds.add(guild)
        skills.update(skill)








obj, created = Person.objects.get_or_create(
    first_name="John",
    last_name="Lennon",
    defaults={"birthday": date(1940, 10, 9)},
)



















if __name__ == "__main__":
    main()
