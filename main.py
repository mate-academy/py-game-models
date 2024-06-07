import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players_file:

        players = json.load(players_file)

    for player_name, player_info in players.items():

        guild = None
        guild_dict = player_info["guild"]
        if isinstance(guild_dict, dict):
            guild = Guild.objects.get_or_create(
                name=guild_dict["name"],
                description=guild_dict["description"]
            )[0]

        race_dict = player_info["race"]
        race = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict["description"]
        )[0]

        for skill in race_dict["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
