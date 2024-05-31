import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    list_of_players = list(players_data)

    for player in list_of_players:
        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=Race.objects.get_or_create(
                name=players_data[player]["race"]["name"],
                description=players_data[player]["race"]["description"]
            )[0],
            guild=Guild.objects.get_or_create(
                name=players_data[player]["guild"]["name"],
                description=players_data[player]["guild"]["description"]
            )[0] if players_data[player]["guild"] is not None else None
        )
        for skill in players_data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=
                                      players_data[player]["race"]["name"])
            ) if skill is not None else None


if __name__ == "__main__":
    main()
