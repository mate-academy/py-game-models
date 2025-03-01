import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def load_players_from_json(file_path):
    with open(file_path, 'r') as file:
        players_data = json.load(file)
    
    for player_data in players_data:
        race, _ = Race.objects.get_or_create(
            name=player_data.get('race', {}).get('name'),
            defaults={'description': player_data.get('race', {}).get('description', '')}
        )
        
        for skill_data in player_data.get('race', {}).get('skills', []):
            Skill.objects.get_or_create(
                name=skill_data.get('name'),
                defaults={'bonus': skill_data.get('bonus'), 'race': race}
            )
        
        guild = None
        guild_data = player_data.get('guild')
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get('name'),
                defaults={'description': guild_data.get('description', '')}
            )
        
        Player.objects.get_or_create(
            nickname=player_data.get('nickname'),
            defaults={
                'email': player_data.get('email'),
                'bio': player_data.get('bio', ''),
                'race': race,
                'guild': guild
            }
        )


if __name__ == "__main__":
    main()
