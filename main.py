import json

from django.core.exceptions import ObjectDoesNotExist
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_char in players.items():
        race_data = player_char["race"]
        guild_data = player_char["guild"]

        race_info, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skills in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=race_info
            )

        if guild_data:
            guild_info, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild_info = None

        try:
            Player.objects.get(
                nickname=player_name,
                email=player_char["email"],
                bio=player_char["bio"],
                race=race_info,
                guild=guild_info
            )
        except ObjectDoesNotExist:
            Player.objects.create(
                nickname=player_name,
                email=player_char["email"],
                bio=player_char["bio"],
                race=race_info,
                guild=guild_info
            )


if __name__ == "__main__":
    main()
