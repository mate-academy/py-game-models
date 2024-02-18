from db.models import Race


def get_skill_data(players: dict) -> dict:
    skill_data = dict()
    for player in players:
        race = Race.objects.get(name=players[player]["race"]["name"])
        skill_data[race] = players[player]["race"]["skills"]
    return skill_data
