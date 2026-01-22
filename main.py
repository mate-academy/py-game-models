import init_django_orm  # noqa: F401
import json
from datetime import datetime
from django.utils.timezone import make_aware
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        players_data = json.load(file)

    for player_data in players_data:
        # Pobierz lub stwórz rasę
        race, created = Race.objects.get_or_create(
            name=player_data['race']['name'],
            defaults={'description': player_data['race'].get('description', '')}
        )

        # Pobierz lub stwórz gildię
        guild, created = Guild.objects.get_or_create(
            name=player_data['guild']['name'],
            defaults={'description': player_data['guild'].get('description', '')}
        )

        # Pobierz lub stwórz umiejętności
        for skill_data in player_data['skills']:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'bonus': float(skill_data['bonus']),
                    # lub float(skill_data['bonus']) jeśli bonusy są liczbami zmiennoprzecinkowymi
                    'race': race
                }
            )

        # Stwórz gracza
        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            defaults={
                'email': player_data['email'],
                'bio': player_data['bio'],
                'race': race,
                'guild': guild,
                'created_at': make_aware(datetime.strptime(player_data['created_at'], '%Y-%m-%d %H:%M:%S'))
            }
        )


if __name__ == "__main__":
    main()
