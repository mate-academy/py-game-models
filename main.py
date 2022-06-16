import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():

    with open("players.json") as f:
        data = json.load(f)

    for name in data:

        # check if race exists
        if Race.objects.filter(name=data[name]["race"]["name"]).exists():
            race = Race.objects.get(name=data[name]["race"]["name"]).id
        else:
            Race.objects.create(name=data[name]["race"]["name"],
                                description=data[name]["race"]["description"])
            race = Race.objects.get(name=data[name]["race"]["name"]).id

        # check_the_skills_exists
        for skill in data[name]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race_id=race)

        # check the guild exists
        if data[name]["guild"]:
            if Guild.objects.filter(name=data[name]["guild"]["name"]).exists():
                guild = Guild.objects.get(name=data[name]["guild"]["name"]).id
            else:
                Guild.objects.create(
                    name=data[name]["guild"]["name"],
                    description=data[name]["guild"]["description"]
                )
                guild = Guild.objects.get(name=data[name]["guild"]["name"]).id
        else:
            guild = None

        # make a player
        Player.objects.create(nickname=name,
                              email=data[name]["email"],
                              bio=data[name]["bio"],
                              race_id=race,
                              guild_id=guild)


if __name__ == "__main__":
    main()
