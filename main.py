import init_django_orm  # noqa: F401
import json
from django.utils import timezone
import datetime


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_name = player_data['race']['name']
        race_description = player_data['race']['description']
        race, created = Race.objects.get_or_create(name=race_name, defaults={'description': race_description})

        for skill_data in player_data['race']['skills']:
            skill_name = skill_data['name']
            skill_bonus = skill_data['bonus']
            Skill.objects.get_or_create(name=skill_name, defaults={'bonus': skill_bonus, 'race': race})

        guild_name = player_data['guild']['name']
        guild_description = player_data['guild']['description']
        guild, created = Guild.objects.get_or_create(name=guild_name, defaults={'description': guild_description})

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild,
            created_at=timezone.make_aware(datetime.datetime.now())
        )


if __name__ == "__main__":
    main()
