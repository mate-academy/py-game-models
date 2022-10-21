import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players_data = json.load(json_file)

    for nickname, player_data in players_data.items():
        if not Race.objects.filter(
            name=player_data["race"]["name"]
        ).exists():
            Race.objects.create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"],
            )
        race = Race.objects.get(name=player_data["race"]["name"])
        if player_data["race"]["skills"]:
            for skill in player_data["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )
        if player_data["guild"]:
            if not Guild.objects.filter(
                name=player_data["guild"]["name"]
            ).exists():
                Guild.objects.create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"],
                )
            guild = Guild.objects.get(name=player_data["guild"]["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
