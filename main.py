import json
from db.models import Race, Skill, Guild, Player
from django.db import transaction

def main():
    with open('players.json', 'r', encoding='utf-8') as f:
        players_data = json.load(f)

    for player_data in players_data:
        # Criar ou obter a raça
        race_name = player_data['race']['name']
        race_description = player_data['race'].get('description', '')
        race, _ = Race.objects.get_or_create(name=race_name, defaults={'description': race_description})

        # Criar ou obter as habilidades da raça
        for skill_data in player_data['race'].get('skills', []):
            skill_name = skill_data['name']
            bonus = skill_data['bonus']
            Skill.objects.get_or_create(name=skill_name, defaults={'bonus': bonus, 'race': race})

        # Criar ou obter a guilda
        guild_info = player_data.get('guild')
        if guild_info:
            guild_name = guild_info['name']
            guild_description = guild_info.get('description')
            guild, _ = Guild.objects.get_or_create(name=guild_name, defaults={'description': guild_description})
        else:
            guild = None

        # Criar o jogador
        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            defaults={
                'email': player_data['email'],
                'bio': player_data['bio'],
                'race': race,
                'guild': guild
            }
        )

if __name__ == "__main__":
    main()
