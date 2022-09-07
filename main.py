import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json') as f:
        data = json.load(f)

    for keys in data:
        guild_in_db = None
        if data[keys]['guild'] is not None:
            guild = Guild(name=data[keys]['guild']['name'],
                          description=data[keys]['guild']['description'])
            if Guild.objects.filter(name=guild.name).exists() is False:
                guild.save()

            guild_in_db = Guild.objects.get(name=data[keys]['guild']['name'])

        race = Race(name=data[keys]['race']['name'],
                    description=data[keys]['race']['description'])
        if Race.objects.filter(name=race.name).exists() is False:
            race.save()

        race_in_db = Race.objects.get(name=data[keys]['race']['name'])

        if len(data[keys]['race']['skills']) != 0:
            for skill in data[keys]['race']['skills']:
                skills = Skill(name=skill["name"],
                               bonus=skill["bonus"],
                               race=race_in_db)
                if Skill.objects.filter(name=skills.name).exists() is False:
                    skills.save()

        player = Player(nickname=keys,
                        email=data[keys]['email'],
                        bio=data[keys]['bio'],
                        race=race_in_db,
                        guild=guild_in_db,
                        created_at="date_now")
        player.save()


if __name__ == "__main__":
    main()
