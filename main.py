import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # open json
    with open("players.json") as file:
        players = json.load(file)

    # load players into a db
    for player_name, player_content in players.items():

        # load race data
        additional_race_name = player_content["race"]["name"]
        additional_race_description = player_content["race"]["description"]
        if not Race.objects.filter(name=additional_race_name):
            Race.objects.create(name=additional_race_name,
                                description=additional_race_description)

        # load skills data
        skills = player_content["race"]["skills"]
        additional_race = Race.objects.get(name=additional_race_name)
        for skill in skills:
            additional_skill_name = skill["name"]
            additional_skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=additional_skill_name):
                Skill.objects.create(
                    name=additional_skill_name,
                    bonus=additional_skill_bonus,
                    race=additional_race
                )

        # load guild data
        if player_content["guild"] is not None:
            additional_guild_name = player_content["guild"]["name"]
            additional_guild_description = None
            if player_content["guild"]["description"]:
                additional_guild_description =\
                    player_content["guild"]["description"]
            if not Guild.objects.filter(name=additional_guild_name):
                Guild.objects.create(name=additional_guild_name,
                                     description=additional_guild_description)

        # load player data
        additional_guild = None
        if player_content["guild"] is not None:
            additional_guild = Guild.objects.get(
                name=player_content["guild"]["name"]
            )
        Player.objects.create(
            nickname=player_name,
            email=player_content["email"],
            bio=player_content["bio"],
            race=additional_race,
            guild=additional_guild
        )


if __name__ == "__main__":
    main()

    # with open("players.json") as file:
    #     players = json.load(file)
    # print(players["nick"]["guild"])
