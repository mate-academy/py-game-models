import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        player_data = json.load(file)

    for player in player_data:
        if Race.objects.filter(
                name=player_data[player]["race"]["name"]
        ).exists():
            race = Race.objects.get(name=player_data[player]["race"]["name"])
        else:
            race = Race.objects.create(
                name=player_data[player]["race"]["name"],
                description=player_data[player]["race"]["description"]
            )
        if player_data[player]["guild"]:
            if Guild.objects.filter(
                    name=player_data[player]["guild"]["name"]
            ).exists():
                guild = Guild.objects.get(
                    name=player_data[player]["guild"]["name"]
                )
            else:
                guild = Guild.objects.create(
                    name=player_data[player]["guild"]["name"],
                    description=player_data[player]["guild"]["description"]
                )
        else:
            guild = None
        Player.objects.create(
            nickname=player,
            email=player_data[player]["email"],
            bio=player_data[player]["bio"],
            race=race,
            guild=guild
        )
        for skill in player_data[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=player_data[player]["race"]["name"]
                    )
                )


if __name__ == "__main__":
    main()
