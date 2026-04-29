import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # 1. Load data from file (Keeping the context manager small)
    with open("players.json", "r") as file:
        players_data = json.load(file)

    # 2. Process players
    for nickname, data in players_data.items():
        # Handle Race
        race_data = data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        # Handle Skills for this Race
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={"bonus": skill_data.get("bonus")}
            )

        # Handle Guild (can be None)
        guild_info = data.get("guild")
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )

        # Create Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
