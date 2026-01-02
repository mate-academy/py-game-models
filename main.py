import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        # Get or create the race
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data[
                "race"
            ].get("description", "")}
        )

        # Get or create skills for this race
        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # Get or create the guild (if player has one)
        guild = None
        if player_data.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data[
                    "guild"
                ].get("description")}
            )

        # Create the player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )
