import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_in:
        players = json.load(file_in)

    for player_name, player_attributes in players.items():
        guild_dict = player_attributes["guild"]
        race_dict = player_attributes["race"]
        skills_dict = race_dict["skills"]
        guild_object = None
        race_object = None

        if guild_dict:
            guild_object = Guild.objects.get_or_create(
                name=guild_dict["name"],
                description=guild_dict["description"]
            )[0]
        if race_dict:
            race_object = Race.objects.get_or_create(
                name=race_dict["name"],
                description=race_dict["description"]
            )[0]
        for skill in skills_dict:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_object
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_attributes["email"],
            bio=player_attributes["bio"],
            race=race_object,
            guild=guild_object
        )


if __name__ == "__main__":
    main()
