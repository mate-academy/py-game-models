import json
from db.models import Player, Race, Skill, Guild
from django.utils.timezone import now


def main():
    with open("players.json", "r", encoding="utf-8") as f:
        players_inf = json.load(f)

    for nickname, user_info in players_inf.items():
        race_data = user_info['race']
        race, _ = Race.objects.get_or_create(
            name=race_data['name'],
            defaults={'description': race_data.get('description', '')}
        )

        for skill_data in race_data.get('skills', []):
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'bonus': skill_data['bonus'],
                    'race': race
                }
            )

        guild = None
        if 'guild' in user_info and user_info['guild']:
            guild_data = user_info['guild']
            guild, _ = Guild.objects.get_or_create(
                name=guild_data['name'],
                defaults={'description': guild_data.get('description')}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                'email': user_info.get('email', ''),
                'bio': user_info.get('bio', ''),
                'race': race,
                'guild': guild,
                'created_at': now()
            }
        )
