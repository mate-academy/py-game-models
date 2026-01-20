import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players_data = json.load(json_file)

    for player in players_data:
        race = players_data[player].get("race")
        new_race = None
        if race:
            new_race, _ = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )
            skills = race.get("skills", [])
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=new_race
                )

        guild = players_data[player].get("guild")
        new_guild = None
        if guild:
            new_guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.create(
            nickname=player,
            email=players_data[player].get("email"),
            bio=players_data[player].get("bio"),
            race_id=new_race.id if new_race else None,
            guild_id=new_guild.id if new_guild else None
        )


if __name__ == "__main__":
    main()
