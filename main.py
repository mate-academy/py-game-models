import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player_name, player_info in players_data.items():
        # Get or create Race
        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data.get("description", "")
            }
        )

        # Create skills for the race
        skills = race_data.get("skills", [])
        for skill_data in skills:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        # Get or create Guild
        guild_data = player_info.get("guild", {})
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description", "")
                }
            )

        # Create Player
        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
