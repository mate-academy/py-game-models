import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        read_file = json.load(file)
        for nickname, player_info in read_file.items():
            if not Race.objects.filter(
                    name=player_info["race"]["name"]).exists():
                race_instance = Race.objects.create(
                    name=player_info["race"]["name"],
                    description=player_info["race"]["description"])
            for skill_dict in player_info["race"]["skills"]:
                if not Skill.objects.filter(name=skill_dict["name"]).exists():
                    Skill.objects.create(name=skill_dict["name"],
                                         bonus=skill_dict["bonus"],
                                         race=race_instance)
            if player_info["guild"] is not None and \
                    not Guild.objects.filter(
                        name=player_info["guild"]["name"]).exists():
                guid_instance = Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"])
            if player_info["guild"] is None:
                guid_instance = None
            if not Player.objects.filter(nickname=nickname).exists():
                Player.objects.create(nickname=nickname,
                                      email=player_info["email"],
                                      bio=player_info["bio"],
                                      race=race_instance,
                                      guild=guid_instance)


if __name__ == "__main__":
    main()
