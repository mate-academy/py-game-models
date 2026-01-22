import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as f:
        players = json.load(f)

    for player in players:
        race_data = player.get('race')
        if not race_data:
            continue
        race_obj, created = Race.objects.get_or_create(
            name=race_data.get('name'),
            defaults={'description': race_data.get('description', '')}
        )

        for skill in race_data.get('skills', []):
            Skill.objects.get_or_create(
                name=skill.get('name'),
                race=race_obj,
                defaults={'bonus': skill.get('bonus')}
            )

        guild_obj = None
        guild_data = player.get('guild')
        if guild_data:
            guild_obj, created = Guild.objects.get_or_create(
                name=guild_data.get('name'),
                defaults={'description': guild_data.get('description')}
            )

        Player.objects.get_or_create(
            nickname=player.get('nickname'),
            defaults={
            'email': player.get('email'),
            'bio': player.get('bio'),
            'race': race_obj,
            'guild': guild_obj
            }
        )


if __name__ == "__main__":
    main()
