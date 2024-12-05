import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:

    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():

        race_data = player_data.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", ""),
            defaults={
                "description": race_data.get("description", "")
            }
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data.get("name", ""),
                bonus=skill_data.get("bonus", ""),
                race=race
            )

        guild = None
        guild_data = player_data.get("guild", {})
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", ""),
                defaults={
                    "description": guild_data.get("description", "")
                }
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
