import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        players_data = json.load(file)

        for user_name, value in players_data.items():
            print("key:", user_name, "value:", value)
            if not Player.objects.filter(nickname=user_name).exists():
                temp_race = None
                if not Race.objects.filter(
                        name=value['race']['name']).exists():
                    temp_race = Race.objects.create(
                        name=value['race']['name'],
                        description=value['race']['description'])
                else:
                    temp_race = Race.objects.get(
                        name=value['race']['name'])

                for skill in value['race']['skills']:
                    if not Skill.objects.filter(
                            name=skill['name']).exists():
                        Skill.objects.create(name=skill['name'],
                                             bonus=skill['bonus'],
                                             race=temp_race)

                if value['guild'] is not None \
                        and not Guild.objects.filter(
                            name=value['guild']['name']).exists():
                    temp_guild = Guild.objects.create(
                        name=value['guild']['name'],
                        description=value['guild']['description'])

                Player.objects.create(nickname=user_name,
                                      email=value['email'],
                                      bio=value['bio'],
                                      race=temp_race,
                                      guild=temp_guild
                                      if value['guild'] is not None
                                      else None)


if __name__ == "__main__":
    Skill.objects.all().delete()
    Race.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    main()
