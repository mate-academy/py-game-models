import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as players_data:
        users_data = json.load(players_data)

    for player in users_data:
        name_race = users_data[player]["race"]["name"]
        skills_ = users_data[player]["race"]["skills"]
        name_skills = skills_[0]["name"] if skills_ else []
        guild = users_data[player]["guild"]
        name_guild = guild["name"] if guild else None
        description_guild = guild["description"]if guild else None

        if not Race.objects.filter(name=name_race).exists():
            Race.objects.create(
                name=name_race,
                description=users_data[player]["race"]["description"]
            )

        if skills_ and not Skill.objects.filter(name=name_skills).exists():
            for i in range(len(skills_)):
                Skill.objects.create(
                    name=users_data[player]["race"]["skills"][i]["name"],
                    bonus=users_data[player]["race"]["skills"][i]["bonus"],
                    race=Race.objects.filter(name=name_race)[0]
                )

        if not Guild.objects.filter(name=name_guild).exists() and name_guild:
            Guild.objects.create(
                name=name_guild,
                description=description_guild if description_guild else None
            )

        Player.objects.create(
            nickname=player,
            email=users_data[player]["email"],
            bio=users_data[player]["bio"],
            race=Race.objects.filter(name=name_race)[0],
            guild=Guild.objects.filter(
                name=name_guild
            )[0] if name_guild else None
        )


if __name__ == "__main__":
    main()
