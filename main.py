import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        players_data = json.load(data)

    for player in players_data:
        # Guild
        if players_data[player].get("guild"):
            if Guild.objects.filter(
                    name=players_data[player]["guild"]["name"]
            ).exists():
                player_guild = Guild.objects.get(
                    name=players_data[player]["guild"]["name"]
                )
            else:
                player_guild = Guild.objects.create(
                    name=players_data[player]["guild"]["name"],
                    description=players_data[player]["guild"]["description"]
                )
        else:
            player_guild = None
        # Race
        if Race.objects.filter(
                name=players_data[player]["race"]["name"]
        ).exists():
            Race.objects.get(name=players_data[player]["race"]["name"])

        else:
            Race.objects.create(
                name=players_data[player]["race"]["name"],
                description=players_data[player]["race"]["description"]
            )

        # Skills
        if skills := players_data[player]["race"]["skills"]:

            for skill in skills:
                if Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.get(name=skill["name"])

                else:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(
                            name=players_data[player]["race"]["name"]
                        )
                    )

        # Player

        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=Race.objects.get(name=players_data[player]["race"]["name"]),
            guild=player_guild,
        )


if __name__ == "__main__":
    main()
