import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        data = json.load(data_file)
        for checker in data:
            race_name = data.get(checker).get("race").get("name")
            if Race.objects.filter(
                    name=race_name).exists() is False:
                properties = data.get(checker).get("race").get("description")
                race_hero = Race.objects.create(
                    name=data.get(checker).get("race").get("name"),
                    description=properties)
            if data.get(checker).get("guild") is not None:
                guild_check = data.get(checker).get("guild").get("name")
            if data.get(checker).get("guild") is None:
                guild_name = None
            if Guild.objects.filter(name=guild_check).exists() is False:
                descript = data.get(checker).get("guild").get("description")
                guild_name = Guild.objects.create(
                    name=data.get(checker).get("guild").get("name"),
                    description=descript)
            if Player.objects.filter(nickname=checker).exists() is False:
                Player.objects.create(
                    nickname=checker,
                    email=data.get(checker).get("email"),
                    bio=data.get(checker).get("bio"),
                    race=race_hero,
                    guild=guild_name)
            skills = data.get(checker).get("race").get("skills")
            for skill in skills:
                if Skill.objects.filter(
                        name=skill.get("name")).exists() is False:
                    Skill.objects.create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race_hero)


if __name__ == "__main__":
    main()
