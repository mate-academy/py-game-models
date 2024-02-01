import json
from datetime import datetime

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", ""),
            description=race_data.get("description", "")
        )

        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", ""),
                description=guild_data.get("description", "")
            )
        else:
            guild = None

        skills = []
        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data.get("name", ""),
                bonus=skill_data.get("bonus", ""),
                race=race
            )
            skills.append(skill)

        try:
            player, created = Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": player_data.get("email", ""),
                    "bio": player_data.get("bio", ""),
                    "race": race,
                    "guild": guild,
                    "created_at": datetime.now()
                }
            )

            if not created:
                player.email = player_data.get("email", "")
                player.bio = player_data.get("bio", "")
                player.race = race
                player.guild = guild
                player.created_at = datetime.now()
                player.save()

            player.skills.set(skills)

        except AttributeError:
            print(f"Player {player_name} already exists")


if __name__ == "__main__":
    main()
