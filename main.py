import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main(file_path = "players.json") -> None:
    with open(file_path, 'r') as file:
        players_data = json.load(file)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(
            name=player_data['race']['name'],
            defaults={'description': player_data['race'].get('description', '')}
        )
        
        for skill_data in player_data['race'].get('skills', []):
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={'bonus': skill_data['bonus'], 'race': race}
            )
        
        guild = None
        if 'guild' in player_data and player_data['guild']:
            guild, _ = Guild.objects.get_or_create(
                name=player_data['guild']['name'],
                defaults={'description': player_data['guild'].get('description', '')}
            )
        
        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            defaults={
                'email': player_data['email'],
                'bio': player_data.get('bio', ''),
                'race': race,
                'guild': guild
            }
        )


if __name__ == "__main__":
    main()
