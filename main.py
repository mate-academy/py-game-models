import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        file_with_players = json.load(players_file)
        for player in file_with_players:
            print(file_with_players[player]["guild"])
            if not Race.objects.filter(name=file_with_players[player]["race"]["name"]).exists():
                new_race = Race.objects.create(
                    name=file_with_players[player]["race"]["name"],
                    description=file_with_players[player]["race"]["description"]
                )
                for skill in file_with_players[player]["race"]["skills"]:
                    new_skill = Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=new_race
                    )
            if file_with_players[player]["guild"] is not None and not Guild.objects.filter(name=file_with_players[player]["guild"]["name"]).exists():
                new_guild = Guild.objects.create(
                    name=file_with_players[player]["guild"]["name"],
                    description=file_with_players[player]["guild"]["description"]
                )
            Player.objects.create(
                nickname=player,
                email=file_with_players[player]["email"],
                bio=file_with_players[player]["bio"],
                race=Race.objects.get(name=file_with_players[player]["race"]["name"]),
                guild=Guild.objects.get(name=file_with_players[player]["guild"]["name"])
            )


if __name__ == "__main__":
    main()
