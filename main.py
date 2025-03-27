import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def main():
    # Завантажуємо дані з файлу players.json
    with open('players.json', 'r') as f:
        data = json.load(f)

    for player_name, player_data in data.items():
        # Перевіряємо, чи існує расу
        race, created = Race.objects.get_or_create(
            name=player_data['race']['name'],
            defaults={'description': player_data['race'].get('description', '')}
        )

        # Створюємо навички для раси
        for skill_data in player_data['race']['skills']:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                bonus=skill_data['bonus'],
                race=race
            )

        # Перевіряємо, чи існує гільдія
        if player_data['guild']:
            guild, created = Guild.objects.get_or_create(
                name=player_data['guild']['name'],
                defaults={'description': player_data['guild'].get('description', '')}
            )
        else:
            guild = None

        # Створюємо гравця
        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()