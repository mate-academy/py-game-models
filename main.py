import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)

    for player, player_data in players.items():
        if guild_info := player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(**guild_info)
        else:
            guild = None

        rase_info = player_data["race"]
        race, race_is_created = Race.objects.get_or_create(
            name=rase_info["name"],
            description=rase_info["description"]
        )

        if rase_info["skills"] and race_is_created:
            for skill_data in rase_info["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race,
                )

        Player.objects.create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
