import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for nickname_, properties in players.items():

        users_guild = None

        race = Race.objects.get_or_create(
            name=properties["race"]["name"],
            description=properties["race"]["description"],
        )[0]

        for skill in properties["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if properties["guild"]:
            users_guild = Guild.objects.get_or_create(
                name=properties["guild"]["name"],
                description=properties["guild"]["description"]
            )[0]

        Player.objects.create(
            nickname=nickname_,
            email=properties["email"],
            bio=properties["bio"],
            race=race,
            guild=users_guild
        )


if __name__ == "__main__":
    main()
