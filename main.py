import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    players_json_content = {}
    with open("players.json") as file:
        data = json.load(file)
        players_json_content.update(data)

    for item in players_json_content:
        our_player = players_json_content[item]
        if not Race.objects.filter(name=our_player["race"]["name"]).exists():
            player_race = Race.objects.\
                create(name=our_player["race"]["name"],
                       description=our_player["race"]["description"],
                       )

        for skill in our_player["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=player_race,
                                     )

        if our_player["guild"] is not None and \
                not Guild.objects.\
                filter(name=our_player["guild"]["name"]).exists():
            player_guild = Guild.objects.\
                create(name=our_player["guild"]["name"],
                       description=our_player["guild"]["description"],
                       )

        if our_player["guild"] is None:
            player_guild = None

        Player.objects.create(nickname=item,
                              email=our_player["email"],
                              bio=our_player["bio"],
                              race=player_race,
                              guild=player_guild
                              )


if __name__ == "__main__":
    main()
