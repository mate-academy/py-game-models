from json import load

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = load(file)

    for player in players_data:
        player_info = players_data[player]

        race, _ = Race.objects.get_or_create(
            name=player_info.get("race").get("name"),
            description=player_info.get("race").get("description"),
        ) if player_info.get("race").get("description") else None

        if player_info.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player_info.get("guild").get("name"),
                description=player_info.get("guild").get("description")
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )

        skills_info = player_info.get("race").get("skills")
        for skill in skills_info:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )


if __name__ == "__main__":
    main()
