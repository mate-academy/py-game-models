import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, other_info in data.items():

        player_email = other_info["email"]
        player_bio = other_info["bio"]
        player_race = other_info["race"]
        player_guild = other_info["guild"]
        player_skills = player_race["skills"]

        if not Race.objects.filter(name=player_race["name"]).exists():
            Race.objects.create(
                name=player_race["name"],
                description=player_race["description"]
            )
        player_race = Race.objects.get(name=player_race["name"])

        if player_guild:
            if not Guild.objects.filter(name=player_guild["name"]).exists():
                Guild.objects.create(
                    name=other_info["guild"]["name"],
                    description=other_info["guild"]["description"]
                )
            player_guild = Guild.objects.get(name=player_guild["name"])
        else:
            player_guild = None

        for skill in player_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_email,
                bio=player_bio,
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
