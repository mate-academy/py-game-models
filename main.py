import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # open json
    with open("players.json") as file:
        players = json.load(file)

    def race_loading(name: str, description: str) -> None:
        if not Race.objects.filter(name=name):
            Race.objects.create(
                name=name,
                description=description
            )

    def skills_loading(skills: list, race_name: Race) -> None:
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_name
                )

    def guild_loading(name: str, description: str) -> None:
        if not Guild.objects.filter(name=name):
            Guild.objects.create(
                name=name,
                description=description)

    # load players into a db
    for player_name, player_content in players.items():

        # load race data
        race_loading(
            name=player_content["race"]["name"],
            description=player_content["race"]["description"]
        )

        # load skills data
        skills_loading(
            skills=player_content["race"]["skills"],
            race_name=Race.objects.get(name=player_content["race"]["name"])
        )

        # load guild data
        if player_content["guild"] is not None:
            guild_loading(
                name=player_content["guild"]["name"],
                description=player_content["guild"]["description"]
            )
            additional_guild = Guild.objects.get(
                name=player_content["guild"]["name"]
            )
        else:
            additional_guild = None

        # load player data
        additional_race = Race.objects.get(name=player_content["race"]["name"])
        Player.objects.create(
            nickname=player_name,
            email=player_content["email"],
            bio=player_content["bio"],
            race=additional_race,
            guild=additional_guild
        )


if __name__ == "__main__":
    main()
