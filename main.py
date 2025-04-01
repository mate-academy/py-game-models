import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r', encoding='utf-8') as file:
        players_data = json.load(file)

    for player_data in players_data:
        race, created = Race.objects.get_or_create(
            name=player_data['race']['name'],
            defaults={'description': player_data['race'].get('description', '')}
        )

        for skill_data in player_data['race']['skills']:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                bonus=skill_data['bonus'],
                race=race
            )

        guild, created = Guild.objects.get_or_create(
            name=player_data['guild']['name'],
            defaults={'description': player_data['guild'].get('description', '')}
        )

        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
