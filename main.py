import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Load data from players.json
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for name, player in players_data.items():
        # Handle Race
        race_data = player.get("race")
        race = None
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

        # Handle Skills for the Race
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # Handle Guild
        guild_data = player.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        # Handle Player
        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
