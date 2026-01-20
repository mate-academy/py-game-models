import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as list_players:
        info_players = json.load(list_players)

    for player_name, game_info_player in info_players.items():
        # create Race
        if not Race.objects.filter(
                name=game_info_player["race"]["name"]
        ).exists():
            race = Race.objects.create(
                name=game_info_player["race"]["name"],
                description=game_info_player["race"]["description"],
            )
        else:
            race = Race.objects.get(name=game_info_player["race"]["name"])

        # create Skill
        for skill_player in game_info_player["race"]["skills"]:
            if not Skill.objects.filter(
                    name=skill_player["name"]
            ).exists():
                Skill.objects.create(
                    name=skill_player["name"],
                    bonus=skill_player["bonus"],
                    race=race
                )
            else:
                Skill.objects.get(
                    name=skill_player["name"]
                )

        # create Guid
        if game_info_player["guild"] is not None:
            if not Guild.objects.filter(
                    name=game_info_player["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=game_info_player["guild"]["name"],
                    description=game_info_player["guild"]["description"],
                )
            else:
                guild = Guild.objects.get(
                    name=game_info_player["guild"]["name"]
                )
        else:
            guild = None

        # create Player
        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=game_info_player["email"],
                bio=game_info_player["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
