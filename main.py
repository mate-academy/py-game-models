import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player in players_data.items():
        race_data = player.get("race", {})
        skills_data = race_data.get("skills", [])
        guild_data = player.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", ""))

        for skill_data in skills_data:
            Skill.objects.get_or_create(race=race, **skill_data)

        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(**guild_data)

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player.get("email"),
                "bio": player.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
