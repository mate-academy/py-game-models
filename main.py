import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.pop("race")
        guild_data = player_data.pop("guild")

        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"]
            }
        )

        if created:
            for skill_data in race_data["skills"]:
                Skill.objects.create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )

        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
            )
            guild.description = guild_data["description"]
            guild.save()
            player_data["guild"] = guild

        player_data["race"] = race
        player_data["nickname"] = nickname

        Player.objects.update_or_create(
            nickname=player_data["nickname"],
            defaults=player_data
        )


if __name__ == "__main__":
    main()
