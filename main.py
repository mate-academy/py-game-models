import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json', 'r') as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data['race']['name'],
            defaults={'description': player_data['race'].get('description', '')}  # Allow empty description
        )

        guild_data = player_data['guild']
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data['name'],
                defaults={'description': guild_data.get('description', '')}  # Allow empty description
            )
        else:
            guild = None

        for skill_data in player_data['race']['skills']:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data['name'],
                bonus=skill_data['bonus'],
                race=race
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
