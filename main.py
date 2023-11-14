import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild

from datetime import datetime
from django.utils import timezone


def main() -> None:
    # Read data from players.json
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():

        # Get or create Race instance
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]})

        # Get or create Guild instance
        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")})

        # Get or create Skill instances
        skills_data = player_data["race"]["skills"]
        skills = []
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race)

            skills.append(skill)

        # Create Player instance
        Player.objects.get_or_create(nickname=player_name,
                                     email=player_data["email"],
                                     bio=player_data["bio"],
                                     race=race,
                                     guild=guild,
                                     created_at=timezone.make_aware
                                     (datetime.now()))


if __name__ == "__main__":
    main()
