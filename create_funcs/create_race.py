from data_from_players.get_race_data import get_race_data

from db.models import Race
from players_json import players_data


def create_race() -> Race:
    race_data = get_race_data(players_data)
    for race in race_data:
        Race.objects.get_or_create(
            name=race,
            description=race_data[race],
        )
    return Race.objects
