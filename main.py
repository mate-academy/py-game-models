import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json') as f:
        data = json.load(f)

    player = data.get('john', {}).get('race')
    Race.objects.get_or_create(
         name=player['name'],
         description=player['description'],
     )
    print(Race.objects.all())

    guilds = data.get('john', {}).get('guild')
    Guild.objects.get_or_create(
        name=guilds['name'],
        description=guilds['description'],
    )
    print(Guild.objects.all())

    skills = data.get('john', {}).get('race').get('skills')
    skill = skills[1]
    Skill.objects.create(
        name=skill['name'],
        bonus=skill['bonus'],
        race_id=5
    )
    print(Skill.objects.all())

    player_data = data['john']
    for player_name in data:
        if player_name == 'john':
            Player.objects.create(
                nickname=player_name,
                email=player_data.get('email'),
                bio=player_data.get('bio'),
                race_id=5,
                guild_id=3,
            )

    print(Player.objects.all())


if __name__ == "__main__":
    main()
