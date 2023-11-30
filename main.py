import json

from django.db import transaction

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json') as f:
        players_data = json.load(f)

    with transaction.atomic():
        for player_data in players_data:
            race, created = Race.objects.get_or_create(
                name=player_data['race']['name'],
                defaults={'description': player_data['race']['description']}
            )

            guild, created = Guild.objects.get_or_create(
                name=player_data['guild']['name'],
                defaults={'description': player_data['guild']['description']}
            )

            player, created = Player.objects.get_or_create(
                nickname=player_data['nickname'],
                email=player_data['email'],
                bio=player_data['bio'],
                race=race,
                guild=guild
            )

            for skill_data in player_data['skills']:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data['name'],
                    bonus=skill_data['bonus'],
                    race=race
                )


if __name__ == "__main__":
    main()
