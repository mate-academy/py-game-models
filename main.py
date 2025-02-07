import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    for player in players:
        race = None
        if players[player]["race"]:
            race, _ = (Race.objects.get_or_create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"],))
        guild = None
        if players[player]["guild"]:
            guild, _ = (Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"], ))
        for skill in players[player]["race"]["skills"]:
            if players[player]["race"]["skills"]:
                Skill.objects.get_or_create(name=skill["name"],
                                            bonus=skill["bonus"],
                                            race=race)
        Player.objects.get_or_create(nickname=player,
                                     email=players[player]["email"],
                                     bio=players[player]["bio"],
                                     race=race,
                                     guild=guild,)


if __name__ == "__main__":
    main()
