import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as all_players_values:
        all_players = json.load(all_players_values)

    # {'email': 'nick@gmail.com', 'bio': "Hello, I'm Nick",
    #  'race': {'name': 'human', 'description': 'Human race', 'skills': []},
    #  'guild': None}

    for player in all_players:
        person = all_players[player]

        email = person["email"]
        bio = person["bio"]
        race = person["race"]
        race_name = person["race"]["name"]
        race_description = person["race"]["description"]
        race_skills = person["race"]["skills"]

        print(f"\n{player}")
        print(f"EMAIL: {email}")
        print(f"BIO: {bio}")
        print(f"RACE NAME: {race_name}")
        print(f"RACE DESCRIPTION: {race_description}")

        print("SKILLS:")
        for value in race_skills:
            print(value["name"], ": ", value["bonus"])

        Player.objects.create(
            nickname=player,
            email=email,
            bio=bio,
            race=Race.objects.create(
                name=race_name,
                description=race_description))


if __name__ == "__main__":
    main()
