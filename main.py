import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_inf:
        data = json.load(data_inf)

    for key, value in data.items():
        email = value["email"]
        bio = value["bio"]
        race_name = value["race"]["name"]
        race_desc = value["race"]["description"]
        try:
            race = Race.objects.get(name=race_name)
        except Race.DoesNotExist:
            race = Race(name=race_name, description=race_desc)
            race.save()
        if value["guild"] is not None:
            guild_name = value["guild"]["name"]
            guild_desc = value["guild"]["description"]
            try:
                guild = Guild.objects.get(name=guild_name)
            except Guild.DoesNotExist:
                guild = Guild(name=guild_name, description=guild_desc)
                guild.save()
        else:
            guild.id = None

        player = Player(
            nickname=key,
            email=email,
            bio=bio,
            race_id=race.id,
            guild_id=guild.id
        )
        try:
            Player.objects.get(nickname=key)
        except Player.DoesNotExist:
            player.save()
        skills_list = value["race"]["skills"]
        for i in skills_list:
            try:
                Skill.objects.get(name=i["name"])
            except Skill.DoesNotExist:
                skills = Skill(
                    name=i["name"],
                    bonus=i["bonus"],
                    race_id=race.id
                )
                skills.save()


if __name__ == "__main__":
    main()
