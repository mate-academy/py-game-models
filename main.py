import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as dict_players:
        players = json.loads(dict_players.read())

        for nick in players:
            skills = players[nick]["race"]["skills"]
            race = players[nick]["race"]
            player = players[nick]

            if not Race.objects.filter(name=race["name"]).exists():
                Race.objects.create(
                    name=race["name"],
                    description=race["description"]
                )
            player_race = Race.objects.get(name=race["name"])

            guild_players = None
            if player["guild"]:
                guide = player["guild"]
                if not Guild.objects.filter(name=guide["name"]).exists():
                    Guild.objects.create(
                        name=guide["name"],
                        description=guide["description"]
                    )
                guild_players = Guild.objects.get(name=guide["name"])

            Player.objects.create(
                nickname=nick,
                email=player["email"],
                bio=player["bio"],
                race=player_race,
                guild=guild_players,
            )

            for item in skills:
                if not Skill.objects.filter(name=item["name"]).exists():
                    Skill.objects.create(
                        name=item["name"],
                        bonus=item["bonus"],
                        race=player_race
                    )


if __name__ == "__main__":
    main()
