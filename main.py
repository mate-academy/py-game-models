import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    for player_name, player_data in players.items():
        race = None
        if player_data["race"]:
            race, _ = (Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"], ))
        guild = None
        if player_data["guild"]:
            guild, _ = (Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"], ))
        for skill in player_data["race"]["skills"]:
            if player_data["race"]["skills"]:
                Skill.objects.get_or_create(name=skill["name"],
                                            bonus=skill["bonus"],
                                            race=race)
        Player.objects.get_or_create(nickname=player_name,
                                     email=player_data["email"],
                                     bio=player_data["bio"],
                                     race=race,
                                     guild=guild, )


if __name__ == "__main__":
    main()
