import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players = json.load(data_file)

    for player, player_data in players.items():

        # add Race data
        race_name = player_data.get("race")["name"]
        race_description = player_data.get("race")["description"]

        if Race.objects.filter(name=race_name).exists():
            player_race = Race.objects.get(name=race_name)
        else:
            player_race = Race.objects.create(
                name=race_name,
                description=race_description
            )

        # add Skill data
        race_skills = player_data.get("race")["skills"]
        if race_skills:
            for skill in race_skills:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                skill_race = Race.objects.get(name=race_name)

                if Skill.objects.filter(name=skill_name).exists():
                    Skill.objects.get(name=skill_name)
                else:
                    Skill.objects.create(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=skill_race
                    )
        #
        # add Guild data
        if player_data.get("guild"):
            guild_name = player_data.get("guild")["name"]
            guild_description = player_data.get("guild")["description"]

            if Guild.objects.filter(name=guild_name).exists():
                player_guild = Guild.objects.get(name=guild_name)
            else:
                player_guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
        else:
            player_guild = None

        # add Player data
        player_nickname = player
        player_email = player_data.get("email")
        player_bio = player_data.get("bio")

        Player.objects.create(
            nickname=player_nickname,
            email=player_email,
            bio=player_bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
