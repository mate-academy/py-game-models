import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as player_json:
        players_data = json.load(player_json)

    for player_nickname, player_info in players_data.items():
        if not Race.objects.filter(name=player_info["race"]["name"]).exists():
            race = Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"],
            )
        else:
            race = Race.objects.get(name=player_info["race"]["name"])

        for skill in player_info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
            else:
                Skill.objects.get(name=skill["name"])

        if (player_info["guild"] and not Guild.objects.filter(
            name=player_info["guild"]["name"]
        ).exists()):
            guild = Guild.objects.create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"],
            )
        elif player_info["guild"]:
            guild = Guild.objects.get(name=player_info["guild"]["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=player_nickname).exists():
            Player.objects.create(
                nickname=player_nickname,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
