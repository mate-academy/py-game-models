import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        players_data = json.load(data)

    for player in players_data:
        # Guild

        if players_data[player].get("guild"):

            guild_name = players_data[player]["guild"]["name"]
            guild_description = players_data[player]["guild"]["description"]

            if Guild.objects.filter(name=guild_name).exists():
                player_guild = Guild.objects.get(name=guild_name)
            else:
                player_guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
        else:
            player_guild = None

        # Race
        race_name = players_data[player]["race"]["name"]
        race_description = players_data[player]["race"]["description"]

        if Race.objects.filter(name=race_name).exists():
            Race.objects.get(name=race_name)

        else:
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        # Skills

        if skills := players_data[player]["race"]["skills"]:

            for skill in skills:
                skill_name = skill["name"]
                if Skill.objects.filter(name=skill_name).exists():
                    Skill.objects.get(name=skill_name)

                else:
                    Skill.objects.create(
                        name=skill_name,
                        bonus=skill["bonus"],
                        race=Race.objects.get(
                            name=race_name
                        )
                    )

        # Player

        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=Race.objects.get(name=race_name),
            guild=player_guild,
        )


if __name__ == "__main__":
    main()
