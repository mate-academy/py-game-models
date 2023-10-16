import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Guild.objects.all().delete()
    with open("players.json", "r") as file:
        data = json.load(file)
        for name in data:
            player_data = data[name]
            player_race = player_data["race"]
            player_guild = player_data["guild"]
            print(player_guild, 'player_guild1')
            if player_guild:
                player_guild = Guild.objects.get_or_create(**player_guild)
                print(player_guild, 'player_guild2')
        # print(name, 'record')
        # print(data[name])
        # Player.objects.create(nickname =name, bio=player_data["bio"], email=player_data["email"], ra)
        # print("data", data)


if __name__ == "__main__":
    main()
