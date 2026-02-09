import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    """Import players from players.json safely and without duplicates."""
    with open('players.json', 'r', encoding='utf-8') as f:
        players_data = json.load(f)

    for player_data in players_data:
        # SAFE access to race
        race_data = player_data.get('race')
        race = None
        if race_data:
            race_name = race_data.get('name')
            if race_name:
                race_description = race_data.get('description', '')
                race, _ = Race.objects.get_or_create(
                    name=race_name,
                    defaults={'description': race_description}
                )
                # Create skills for this race
                skills_data = race_data.get('skills', [])
                for skill_data in skills_data:
                    skill_name = skill_data.get('name')
                    skill_bonus = skill_data.get('bonus', '')
                    if skill_name:
                        Skill.objects.get_or_create(
                            name=skill_name,
                            defaults={'bonus': skill_bonus, 'race': race}
                        )

        # SAFE access to guild
        guild_data = player_data.get('guild')
        guild = None
        if guild_data:
            guild_name = guild_data.get('name')
            if guild_name:
                guild_description = guild_data.get('description')
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={'description': guild_description}
                )

        # Player creation only if race exists
        nickname = player_data.get('nickname')
        email = player_data.get('email', '')
        bio = player_data.get('bio', '')

        if race and nickname:
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    'email': email,
                    'bio': bio,
                    'race': race,
                    'guild': guild
                }
            )
