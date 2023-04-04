import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_card_file:
        data_players = json.load(players_card_file)
        for data_player in data_players.items():
            player = data_player[1]

            # race
            race_name = player['race']['name']
            if Race.objects.filter(name=race_name).exists():
                race = Race.objects.get(name=race_name)
            else:
                race = Race.objects.create(
                    name=race_name,
                    description=player['race']['description']
                )

            # skills
            for skills in player['race']['skills']:
                if not Skill.objects.filter(name=skills['name']).exists():
                    Skill.objects.create(
                        name=skills['name'],
                        bonus=skills['bonus'],
                        race=race
                    )

            # guild
            if player['guild']:
                guild_name = player['guild']['name']
                if Guild.objects.filter(name=guild_name).exists():
                    guild = Guild.objects.get(name=guild_name)
                else:
                    guild = Guild.objects.create(
                        name=guild_name,
                        description=player['guild']['description']
                    )
            else:
                guild = None

            # player
            nickname = data_player[0]
            Player.objects.create(
                nickname=nickname,
                email=player['email'],
                bio=player['bio'],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
