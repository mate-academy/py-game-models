import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_data in data:
        race, _ = Race.objects.get_or_create(
            name=player_data['race']['name'],
            description=player_data['race'].get('description', '')
        )

        for skill_data in player_data['race']['skills']:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                bonus=skill_data['bonus'],
                race=race
            )

        guild, _ = Guild.objects.get_or_create(
            name=player_data['guild']['name'],
            description=player_data['guild'].get('description', None)
        )

        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            email=player_data['email'],
            bio=player_data['bio'],
            race=race,
            guild=guild,
        )

if __name__ == "__main__":
    main()
