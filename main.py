import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nick_name, player_data in data.items():
        curr_race = None
        curr_guild = None

        # Create or get Guild
        guild_data = player_data.get("guild", {})
        if guild_data:
            guild_name, guild_description = guild_data.values()
            curr_guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description,
            )

        # Create or get Race
        race_data = player_data.get("race", {})
        if race_data:
            race_name, race_description, skills_data = race_data.values()
            curr_race, _ = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

            # Create or get Skills
            for skill_data in skills_data:
                skill_name = skill_data["name"]
                skill_bonus = skill_data["bonus"]

                skill, _ = Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=curr_race,
                )

        # Create Player
        Player.objects.get_or_create(
            nickname=nick_name,
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            race=curr_race,
            guild=curr_guild,
        )


if __name__ == "__main__":
    main()
