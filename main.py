import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main():
    with open("players.json", "r") as file:
        players_dict = json.load(file)
        for player in players_dict:
            if not Race.objects.filter(
                    name=players_dict[player]["race"]["name"]
            ).exists():
                race = Race.objects.create(
                    name=players_dict[player]["race"]["name"],
                    description=players_dict[player]["race"]["description"]
                )
            else:
                race = Race.objects.get(
                    name=players_dict[player]["race"]["name"]
                )
            for skill in players_dict[player]["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"], bonus=skill["bonus"], race=race
                    )
            if players_dict[player]["guild"]:
                player_info = players_dict[player]
                if not Guild.objects.filter(
                        name=player_info["guild"]["name"]).exists():
                    guild = Guild.objects.create(
                        name=player_info["guild"]["name"],
                        description=player_info["guild"]["description"]
                    )
                else:
                    guild = Guild.objects.get(
                        name=player_info["guild"]["name"]
                    )
            else:
                guild = None

            Player.objects.create(
                nickname=player,
                email=players_dict[player]["email"],
                bio=players_dict[player]["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
