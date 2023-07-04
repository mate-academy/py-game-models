import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild

FILE_NAME = "players.json"


def main() -> None:

    with open(FILE_NAME, "r") as file:
        players = json.load(file)

    for nickname_, value in players.items():

        if not Race.objects.filter(name=value["race"]["name"]).exists():
            Race.objects.create(name=value["race"]["name"],
                                description=value["race"]["description"])

        player_race = Race.objects.get(name=value["race"]["name"])

        if value["guild"]:
            if not Guild.objects.filter(name=value["guild"]["name"]).exists():
                Guild.objects.create(name=value["guild"]["name"],
                                     description=value["guild"]["description"])

            player_guild = Guild.objects.get(name=value["guild"]["name"])

        for skill in value["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        if not Player.objects.filter(nickname=nickname_).exists():
            Player.objects.create(
                nickname=nickname_,
                email=value["email"],
                bio=value["bio"],
                race=player_race,
                guild=player_guild
            )

        player_race = None
        player_guild = None


if __name__ == "__main__":
    main()
