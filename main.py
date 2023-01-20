import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        info_file = json.load(file)

    for player_name, player_info in info_file.items():

        race_dict = player_info["race"]
        guild_dict = player_info["guild"]

        if not Race.objects.filter(
            name=race_dict["name"]
        ).exists():
            race = Race.objects.create(
                name=race_dict["name"],
                description=race_dict["description"]
            )
        else:
            race = Race.objects.get(name=race_dict["name"])

        for skill in race_dict["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
            else:
                Skill.objects.get(name=skill["name"])

        if guild_dict is None:
            guild = None
        else:
            if not Guild.objects.filter(
                name=guild_dict["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=guild_dict["name"],
                    description=guild_dict["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_dict["name"])

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild,
            )
        else:
            Player.objects.get(nickname=player_name)


if __name__ == "__main__":
    main()
