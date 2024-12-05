import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:
        player_data = players.get(player)

        race_data = player_data.get("race")
        skills_data = race_data.get("skills")
        guild_data = player_data.get("guild")

        race, is_race_created = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        if skills_data:
            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        if guild_data:
            guild, is_quild_created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
