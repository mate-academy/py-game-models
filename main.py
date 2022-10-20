import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for players_name, other_info in data.items():

        players_email = other_info["email"]
        players_bio = other_info["bio"]
        players_race = other_info["race"]
        players_guild = other_info["guild"]
        players_skills = players_race["skills"]

        if not Race.objects.filter(name=players_race["name"]).exists():
            Race.objects.create(
                name=players_race["name"],
                description=players_race["description"]
            )
        players_race = Race.objects.get(name=players_race["name"])

        if players_guild:
            if not Guild.objects.filter(name=players_guild["name"]).exists():
                Guild.objects.create(
                    name=other_info["guild"]["name"],
                    description=other_info["guild"]["description"]
                )
            players_guild = Guild.objects.get(name=players_guild["name"])
        else:
            players_guild = None

        for skill in players_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=players_race
                )

        if not Player.objects.filter(nickname=players_name).exists():
            Player.objects.create(
                nickname=players_name,
                email=players_email,
                bio=players_bio,
                race=players_race,
                guild=players_guild
            )


if __name__ == "__main__":
    main()
