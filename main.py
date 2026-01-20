import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        players_data = json.load(data)

    for player in players_data:

        player_guild = None
        if players_data[player].get("guild"):

            guild_name = players_data[player]["guild"]["name"]
            guild_description = players_data[player]["guild"]["description"]

            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            player_guild = Guild.objects.get(name=guild_name)

        race_name = players_data[player]["race"]["name"]
        race_description = players_data[player]["race"]["description"]

        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )
        race = Race.objects.get(name=race_name)

        if skills := players_data[player]["race"]["skills"]:
            for skill in skills:
                skill_name = skill["name"]
                if not Skill.objects.filter(name=skill_name).exists():
                    Skill.objects.create(
                        name=skill_name,
                        bonus=skill["bonus"],
                        race=race
                    )

        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=race,
            guild=player_guild,
        )


if __name__ == "__main__":
    main()
