from db.models import Skill
from player_moduls.race_func import race_func


def skill_func(player: dict) -> None:
    for skill in player["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_func(player)}
            )
