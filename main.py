import json
import os
import django
from django.utils import timezone
from db.models import Race, Skill, Player, Guild

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name")
        race_description = race_data.get("description", "")

        race, _ = Race.objects.get_or_create(name=race_name, defaults={"description": race_description})

        skills = race_data.get("skills", [])
        for skill_data in skills:
            skill_name = skill_data.get("name")
            skill_bonus = skill_data.get("bonus")
            Skill.objects.get_or_create(name=skill_name, bonus=skill_bonus, race=race)

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description", "")
            guild, _ = Guild.objects.get_or_create(name=guild_name, defaults={"description": guild_description})

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild,
            created_at=timezone.now()
        )


if __name__ == "__main__":
    main()
