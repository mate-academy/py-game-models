from db.models import Race


def race_func(player: dict):
    if not Race.objects.filter(name=player["race"]["name"]).exists():
        race_inst, created = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
            )
        return race_inst
