import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        data = json.load(file)

        for name, info in data.items():
            race_type = info.get('race')
            guild = info.get('guild')

            race = Race.objects.get_or_create(name=race_type.get('name'), description=race_type.get('description'))[0]
            if skills := race_type.get('skills'):
                _ = [
                    Skill.objects.get_or_create(
                        name=skill.get('name'), bonus=skill.get('bonus'), race=race
                    ) for skill in skills
                ]
            if guild:
                guild = Guild.objects.get_or_create(name=guild.get('name'), description=guild.get('description'))[0]

            Player.objects.create(nickname=name, email=info.get('email'), bio=info.get('bio'), race=race, guild=guild)


if __name__ == "__main__":
    main()
