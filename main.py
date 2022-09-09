import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as json_players:
        players = json.load(json_players)
    for players_name, players_data in players.items():
        if not Race.objects.filter(name=players_data["race"]["name"]).exists():
            race_ = Race.objects.create(
                name=players_data["race"]["name"],
                description=players_data["race"]["description"]
            )
            race_.save()
        else:
            race_ = Race.objects.get(name=players_data["race"]["name"])
            race_.save()

        if players_data["guild"] is None:
            guild_ = None
        elif not Guild.objects.filter(
                name=players_data["guild"]["name"]).exists():
            guild_ = Guild.objects.create(
                name=players_data["guild"]["name"],
                description=players_data["guild"]["description"]
            )
            guild_.save()
        else:
            guild_ = Guild.objects.get(name=players_data["guild"]["name"])
            guild_.save()

        for skill in players_data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_
                )

        Player.objects.create(
            nickname=players_name,
            email=players_data["email"],
            bio=players_data["bio"],
            race=race_,
            guild=guild_
        )


if __name__ == "__main__":
    main()
