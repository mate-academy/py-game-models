import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_json:
        players_data = json.load(players_json)

    for player_name, character in players_data.items():
        race_name = character["race"]["name"]

        if not Race.objects.filter(name=race_name).exists():
            race = Race.objects.create(
                name=race_name,
                description=character["race"]["description"]
            )
        else:
            race = Race.objects.get(name=race_name)

        guild = None
        if character["guild"]:
            guild_name = character["guild"]["name"]
            if not Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.create(
                    name=guild_name,
                    description=character["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_name)

        for skill in character["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=character["email"],
                bio=character["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
