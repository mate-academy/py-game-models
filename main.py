import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    with open("players.json", "r+") as players:
        players_data = json.load(players)

        for nickname, player_data in players_data.items():
            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(name=race_data["name"],
                                                 description=race_data["description"])  # noqa: 501

            for skill in race_data["skills"]:
                Skill.objects.get_or_create(name=skill["name"],
                                            bonus=skill["bonus"],
                                            race=race)

            guild_data = player_data.get("guild")
            if guild_data:
                guild, _ = Guild.objects.get_or_create(name=guild_data["name"],
                                                       description=guild_data.get("description"))  # noqa: 501
            else:
                guild = None

            Player.objects.get_or_create(nickname=nickname,
                                         email=player_data["email"],
                                         bio=player_data["bio"],
                                         race=race, guild=guild)


if __name__ == "__main__":
    main()
