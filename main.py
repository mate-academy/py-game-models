from json import load

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = load(file)

    for player in players_data:
        player_info = players_data[player]

        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"],
        ) if player_info["race"] else None

        if player_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )

        skills_info = player_info["race"]["skills"]
        for skill in skills_info:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
