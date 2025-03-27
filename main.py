import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player in players_data:
        players_info = players_data[player]
        if Race.objects.filter(name=players_info["race"]["name"]).exists():
            player_race = Race.objects.get(name=players_info["race"]["name"])
        else:
            player_race = Race.objects.create(
                name=players_info["race"]["name"],
                description=players_info["race"]["description"])
        for skill in players_info["race"]["skills"]:
            if Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.get(name=skill["name"])
            else:
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=player_race)
        if players_info["guild"]:
            if Guild.objects.filter(
                    name=players_info["guild"]["name"]
            ).exists():
                player_guild = Guild.objects.get(
                    name=players_info["guild"]["name"]
                )
            else:
                player_guild = Guild.objects.create(
                    name=players_info["guild"]["name"],
                    description=players_info["guild"]["description"],
                )
        else:
            player_guild = None
        Player.objects.create(nickname=player,
                              email=players_info["email"],
                              bio=players_info["bio"],
                              race=player_race,
                              guild=player_guild)


if __name__ == "__main__":
    main()
