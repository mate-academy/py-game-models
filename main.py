import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        player_race = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=player_race.get("name"),
            description=player_race.get("description", "")
        )

        for skill_data in player_race.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description", None)
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
