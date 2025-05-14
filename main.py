from django.http import RawPostDataException
from django.core.exceptions import ObjectDoesNotExist
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        data = json.loads(file)
    dictionary = {
            "race": [],
            "skill": [],
            "guild":[]
        }

    for key, value in data.items():
        number_of_skill = 0
        is_race = False
        is_guild = False
        for i in data[key]["race"]["skills"]:
            try:
                Skill.objects.get(name=i["name"])
            except:
                number_of_skill += 1
        try:
            Race.objects.get(name=data[key]["race"]["name"])
        except:
            is_race = True
        try:
            Guild.objects.get(name=data[key]["guild"]["name"])
        except:
            is_guild = True

        if is_race and is_guild and len(data[key]["race"]["skills"]) == number_of_skill:
            race = Race.objects.create(name=data[key]["race"]["name"], description=data[key]["race"]["description"])
            for skill in data[key]["race"]["skills"]:
                Skill.objects.create(name=skill["name"], bonus=skill["bonus"],race=race)
            guild = Guild.objects.create(name=data[key]["guild"]["name"], description=data[key]["guild"]["description"])
            Player.objects.create(nickname=key, email=data[key]["email"], bio=data[key]["bio"],race=race, guild=guild )




if __name__ == "__main__":
    main()
