import json
from db.models import Race, Skill, Guild, Player
from django.db.utils import IntegrityError


def main() -> None:
    with open("players.json", "r") as file:
        player_data = json.load(file)

    data_list = [
        {
            "model": Guild,
            "name": "Example Guild",
            "defaults": {"description": "Example Guild Description"
                         }},
        {
            "model": Race,
            "name": "Example Race",
            "defaults": {"description": "Example Race Description"}
        },
        {
            "model": Skill,
            "name": "Example Skill",
            "bonus": "Example Bonus",
            "race": "Example Race"
        },
    ]

    instances = {}
    for data in data_list:
        model = data["model"]
        name = data["name"]
        defaults = data.get("defaults", {})
        instance, created = (model.objects.get_or_create
                             (name=name, defaults=defaults))
        instances[model] = instance

    for player_info in player_data:
        try:
            player = Player.objects.create(
                nickname=player_info["nickname"],
                email=player_info["email"],
                bio=player_info["bio"],
                race=instances[Race],
                guild=instances[Guild]
            )
            player.save()
            print(f"Player {player.nickname} added to the database.")
        except IntegrityError:
            print(f"Player {player_info['nickname']}"
                  f" already exists in the database.")


if __name__ == "__main__":
    main()
