import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)

    for player_nickname, player_attributes in players_data.items():
        race_name = player_attributes["race"]["name"]
        if not Race.objects.filter(name=race_name).exists():
            race = Race.objects.create(
                name=player_attributes["race"]["name"],
                description=player_attributes["race"]["description"],
            )
            for skill in player_attributes["race"].get("skills"):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        else:
            race = Race.objects.filter(name=race_name).get()
        print(race)

        if player_attributes.get("guild"):
            guild_name = player_attributes["guild"]["name"]
            if not Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.create(
                    name=guild_name,
                    description=player_attributes["guild"].get("description")
                )
            else:
                guild = Guild.objects.filter(name=guild_name).get()
                print(guild)
        else:
            guild = None

        if Player.objects.filter(nickname=player_nickname).exists():
            Player.objects.filter(nickname=player_nickname).update(
                email=player_attributes["email"],
                bio=player_attributes["bio"],
                race=race,
                guild=guild
            )
        else:
            Player.objects.create(
                nickname=player_nickname,
                email=player_attributes["email"],
                bio=player_attributes["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
