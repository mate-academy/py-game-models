import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:
        email = players.get(player).get("email")
        bio = players.get(player).get("bio")
        race = players.get(player).get("race")
        skills = players.get(player).get("race").get("skill")
        guild = players.get(player).get("guild")

        # Trying to create guild for adding it to Player

        try:
            current_guild = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        except AttributeError:
            current_guild = None

        # Creating a race for adding it to Player and Skill

        current_race = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        # Creating a skills from a list

        for skill in skills:

            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=current_race
            )

        # Creating a Player

        if current_guild:
            Player.objects.get_or_create(
                nickname=player,
                email=email,
                bio=bio,
                race=current_race,
                guild=current_guild
            )
        else:
            Player.objects.get_or_create(
                nickname=player,
                email=email,
                bio=bio,
                race=current_race,
            )


if __name__ == "__main__":
    main()
