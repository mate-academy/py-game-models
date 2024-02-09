import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_name, player_details in players.items():
        race, is_created = Race.objects.get_or_create(
            name=player_details["race"]["name"],
            description=player_details["race"]["description"]
        )

        for skill in player_details["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race)

        if player_details["guild"]:
            guild, guild_created = Guild.objects.get_or_create(
                name=player_details["guild"]["name"],
                description=player_details["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_details["email"],
            bio=player_details["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
