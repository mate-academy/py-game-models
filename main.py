import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_name = player_data["race"]["name"]
        race, _ = Race.objects.get_or_create(name=race_name)

        if "race" in player_data:
            race_description = player_data["race"]["description"]
            race.description = race_description
            race.save()
        for skill in player_data["race"]["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]

            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )

        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            guild_description = player_data["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
