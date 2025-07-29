import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, player_info in players.items():
        players_race = player_info["race"]
        race, is_just_created_race = Race.objects.get_or_create(
            name=players_race["name"],
            defaults={"description": players_race["description"]}
        )

        if is_just_created_race:
            for skill_info in players_race.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    race=race,
                    defaults={"bonus": skill_info["bonus"]}
                )

        guild_info = player_info.get("guild")
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info["description"]}
            )

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
