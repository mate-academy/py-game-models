import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json') as players_file:
        players = json.load(players_file)
    for name, player_settings in players.items():
        Player.objects.create(
            nickname=name,
            email=player_settings['email'],
            bio=player_settings['bio'],
            rase=Race.objects.get_or_create(
                name=player_settings['race']['name'],
                description=player_settings['race']['description']
            ),
            guild=Guild.objects.get_or_create(
                name=player_settings['guild']['name'],
                description=player_settings['guild']['description']
            )
        )




if __name__ == "__main__":
    main()
