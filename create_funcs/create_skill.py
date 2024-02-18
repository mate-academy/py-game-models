from data_from_players.get_skill_data import get_skill_data

from db.models import Skill
from players_json import players_data


def create_skill() -> Skill:
    skill_data = get_skill_data(players_data)
    for race in skill_data:
        for skill in skill_data[race]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )
    return Skill.objects
