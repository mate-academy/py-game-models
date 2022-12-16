import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)
    player_race = None
    player_guild = None

    for person in players_data:
        data = players_data[person]
        email_to_add = data["email"]
        person_bio = data["bio"]
        person_race = data["race"]
        person_guild = data["guild"]
        person_skill = data["race"]["skills"]
        if not Race.objects.filter(
            name=person_race["name"], description=person_race["description"]
        ).exists():
            player_race = Race.objects.create(
                name=person_race["name"],
                description=person_race["description"]
            )
        if data["guild"]:
            if Guild.objects.filter(
                    name=person_guild["name"]).exists() is False:
                player_guild = Guild.objects.create(
                    name=person_guild["name"],
                    description=person_guild["description"]
                )

        for skill in person_skill:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=player_race
                )
        Player.objects.create(
            nickname=person,
            email=email_to_add,
            bio=person_bio,
            race=player_race,
            guild=player_guild if data["guild"] else None,
        )


if __name__ == "__main__":
    main()
