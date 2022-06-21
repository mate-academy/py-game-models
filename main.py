import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        nickname = player_name
        data = player_data
        if not Race.objects.filter(name=data["race"]["name"]).exists():
            race = Race.objects.create(name=data["race"]["name"],
                                       description=data["race"]["description"]
                                       )
        else:
            race = Race.objects.get(name=data["race"]["name"])

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race
                                     )

        if data["guild"]:
            if not Guild.objects.filter(
                    name=data["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(
                    name=data["guild"]["name"]
                )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
