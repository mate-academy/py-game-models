import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
        for player_name, value in players.items():
            # Get or create the race
            race, created = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )

            # Handle multiple skills for the race
            for skill_data in value["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                )
                if not created and skill.bonus != skill_data["bonus"]:
                    skill.bonus = skill_data["bonus"]
                    skill.save()

            # Get or create the guild
            guild_data = value.get("guild")
            if guild_data:
                guild_description = guild_data.get("description", '')
                guild, created = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_description
                )
            else:
                guild = None  # Or set to a default guild if needed

            # Get or create the player
            Player.objects.get_or_create(
                nickname=player_name,
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
