import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Load data from the players.json file
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        # Get or create Race
        race_data = player_info["race"]
        race, created_race = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        # Get or create Skills for the Race
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        # Get or create Guild
        guild_data = player_info["guild"]
        if guild_data:
            guild, created_guild = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None

        # Get or create Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
