import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_params in data.items():
        race_params = player_params.get("race")
        race, race_created = Race.objects.get_or_create(
            name=race_params["name"],
            description=race_params["description"]
        )
        if race_created:
            for skill in race_params.get("skills"):
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race
                                     )

        guild_params = player_params.get("guild", None)
        guild = Guild.objects.get_or_create(
            name=guild_params["name"],
            description=guild_params["description"]
        )[0] if guild_params else None

        Player.objects.create(
            nickname=player_name,
            email=player_params["email"],
            bio=player_params["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
