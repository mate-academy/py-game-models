import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json', 'r') as data_file:
        data_player = json.load(data_file)

    for player in data_player:

        if Race.objects.filter(
                name=data_player[player]['race']['name']).exists():
            get_player_race = Race.objects.get(
                name=data_player[player]['race']['name']
            )

        else:
            create_race = Race.objects.create(
                name=data_player[player]['race']['name'],
                description=data_player[player]['race']['description']
            )

            for skill in data_player[player]['race']['skills']:
                Skill.objects.create(
                    name=skill['name'],
                    bonus=skill['bonus'],
                    rece=create_race
                )

            get_player_race = create_race

        if data_player[player]['guild'] is not None:

            if Guild.objects.filter(
                    name=data_player[player]['guild']['name']).exists():

                get_player_guild = Guild.objects.get(
                    name=data_player[player]["guild"]['name']
                )

            else:
                create_guild = Guild.objects.create(
                    name=data_player[player]['guild']['name'],
                    description=data_player[player]['guild']['description']
                )
                get_player_guild = create_guild

        else:
            get_player_guild = None

        Player.objects.create(
            nickname=player,
            email=data_player[player]["email"],
            bio=data_player[player]['bio'],
            race=get_player_race,
            guild=get_player_guild
        )


if __name__ == "__main__":
    main()
