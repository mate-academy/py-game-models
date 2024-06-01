import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as players_file:
        players = json.load(players_file)

    for player, data in players.items():
        guild = None
        if data.get('guild'):
            guild, _ = Guild.objects.get_or_create(
                name=data['guild']['name'],
                description=data['guild']['description']
            )
        race, _ = Race.objects.get_or_create(
            name=data['race']['name'],
            description=data['race']['description']
        )
        for skill in data['race']['skills']:
            Skill.objects.get_or_create(
                name=skill['name'], bonus=skill['bonus'], race=race
            )
        Player.objects.create(
            nickname=player,
            bio=data['bio'],
            email=data['email'],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
