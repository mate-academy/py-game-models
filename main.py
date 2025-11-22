import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_data:
        data = json.load(json_data)

    for player, player_data in data.items():
        if race_data := player_data.get("race"):
            race, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description")
            )

            for skill in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

            guild = None
            if guild_data := player_data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data.get("name"),
                    description=guild_data.get("description")
                )

            Player.objects.create(
                nickname=player,
                email=player_data.get("email"),
                bio=player_data.get("bio"),
                race=race,
                guild=guild
            )
            continue

        raise ValueError("Player cannot be created without race!")


if __name__ == "__main__":
    main()
