import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        players_data = json.load(file)

        for nickname, player_data in players_data.items():
            # Process Race
            race_name = player_data['race']['name']
            race_description = player_data['race'].get('description', '')
            race, _ = Race.objects.get_or_create(name=race_name, defaults={'description': race_description})

            # Process Skills for the Race
            skills = player_data['race'].get('skills', [])
            for skill_data in skills:
                skill_name = skill_data['name']
                skill_bonus = skill_data['bonus']
                Skill.objects.get_or_create(name=skill_name, race=race, defaults={'bonus': skill_bonus})

            # Process Guild
            guild_data = player_data.get('guild')
            guild = None
            if guild_data:
                guild_name = guild_data['name']
                guild_description = guild_data.get('description')
                guild, _ = Guild.objects.get_or_create(name=guild_name, defaults={'description': guild_description})

            # Process Player
            email = player_data['email']
            bio = player_data['bio']
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    'email': email,
                    'bio': bio,
                    'race': race,
                    'guild': guild,
                }
            )

if __name__ == "__main__":
    main()
