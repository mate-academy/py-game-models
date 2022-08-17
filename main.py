import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as players:
        players_dict = json.load(players)
        ls_of_players = list(players_dict.values())

        for player_guild in ls_of_players:
            if player_guild["guild"] is None:
                continue
            if not Guild.objects.filter(
                    name=player_guild["guild"]["name"]).exists():
                Guild.objects.create(
                    name=player_guild["guild"]["name"],
                    description=player_guild["guild"]["description"]
                )

        for race in ls_of_players:
            if not Race.objects.filter(name=race["race"]["name"]).exists():
                Race.objects.create(
                    name=race["race"]["name"],
                    description=race["race"]["description"]
                )

        for skills in ls_of_players:
            for skill in skills["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    race_name = Race.objects.get(name=skills["race"]["name"])
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_name
                    )

        for nickname, config in players_dict.items():
            player_race = Race.objects.get(name=config["race"]["name"])
            if config["guild"] is not None:
                player_guild = Guild.objects.get(name=config["guild"]["name"])
            else:
                player_guild = None

            Player.objects.create(
                nickname=nickname,
                email=config["email"],
                bio=config["bio"],
                race=player_race,
                guild=player_guild,
            )


if __name__ == "__main__":
    main()
