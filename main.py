import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_name = "players.json"
    with open(file_name) as file:
        data = json.load(file)

    for player_name, player_info in data.items():

        if not Race.objects.filter(name=player_info["race"]["name"]):
            Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        race = Race.objects.get(name=player_info["race"]["name"])

        guild = player_info["guild"]
        if guild:
            if not Guild.objects.filter(name=player_info["guild"]["name"]):
                Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"]
                )
            guild = Guild.objects.get(name=player_info["guild"]["name"])
        else:
            guild = None

        for skill in player_info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race)

        Player.objects.create(nickname=player_name,
                              email=player_info["email"],
                              bio=player_info["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
