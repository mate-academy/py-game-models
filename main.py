import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json') as file:
        players_data = json.load(file)
    for player_key, player_data in players_data.items():
        player_race = player_data.get('race')
        race, _ = Race.objects.get_or_create(
            name=player_race['name'],
            defaults={
                'description': player_race['description']
            }
        )
        for skill_data in player_race.get('skills', []):
            Skill.objects.get_or_create(
                    name=skill_data['name'],
                    defaults={
                        'bonus': skill_data['bonus'],
                        'race': race
                    }
                )
        player_guild = player_data.get('guild')
        guild = None
        if player_guild:
            guild, _ = Guild.objects.get_or_create(
                name=player_guild['name'],
                defaults={
                    'description': player_guild['description']
                }
            )
        Player.objects.get_or_create(
            nickname=player_key,
            defaults={
                'email': player_data['email'],
                'bio': player_data['bio'],
                'race': race,
                'guild': guild
            }
        )


if __name__ == '__main__':
    main()
