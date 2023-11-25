import init_django_orm  # noqa: F401
import json
from django.utils import timezone
import datetime


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_data = player_data.get('race', {})
        if race_data:
            race_name = race_data.get('name')
            race_description = race_data.get('description', '')
            race, created = Race.objects.get_or_create(name=race_name, defaults={'description': race_description})

            skills_data = race_data.get('skills', [])
            for skill_data in skills_data:
                skill_name = skill_data.get('name')
                skill_bonus = skill_data.get('bonus')
                Skill.objects.get_or_create(name=skill_name, defaults={'bonus': skill_bonus, 'race': race})

        guild_data = player_data.get('guild', {})
        if guild_data:
            guild_name = guild_data.get('name')
            guild_description = guild_data.get('description', '')
            guild, created = Guild.objects.get_or_create(name=guild_name, defaults={'description': guild_description})

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data.get('email', ''),
            bio=player_data.get('bio', ''),
            race=race,
            guild=guild if guild_data else None,
            created_at=timezone.make_aware(datetime.datetime.now())
        )


if __name__ == "__main__":
    main()
