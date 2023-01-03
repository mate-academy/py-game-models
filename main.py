import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_json:
        players_data = json.load(players_json)

    for player_name, character in players_data.items():

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=character["email"],
                bio=character["bio"],
                race=Race.objects.create(
                    name=character["race"]["name"],
                    description=character["race"]["description"],
                )
                if not Race.objects.filter(name=character["race"]["name"]).exists()
                else Race.objects.get(name=character["race"]["name"]),

                guild=None if character.get("guild") is None else
                Guild.objects.create(
                    name=character["guild"]["name"],
                    description=character["guild"]["description"],
                )
                if not Guild.objects.filter(name=character["guild"]["name"]).exists()
                else Guild.objects.get(name=character["guild"]["name"])
            )

            for skill in character["race"]["skills"]:
                if len(skill) > 0:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=character["race"]["name"])
                    ) \
                        if not Skill.objects.filter(name=skill["name"]).exists() \
                        else Skill.objects.get(name=skill["name"]),


if __name__ == "__main__":
    main()
