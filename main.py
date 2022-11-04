import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild

from skills import Skills as Skill_class

from race import Race as Race_class

from guild import Guild as Guild_class

from player import Player as Player_class


def main() -> None:
    with open("players.json", "r") as data_file:
        data = json.load(data_file)
        for checker in data:
            # object class Race from race.py
            race = Race_class(
                name=data.get(checker).get("race").get("name"),
                description=data.get(checker).get("race").get("description"))
            if Race.objects.filter(name=race.name).exists() is False:
                race_hero = Race.objects.create(name=race.name,
                                                description=race.description)
            skills = data.get(checker).get("race").get("skills")
            skills_update(skills, race_hero)
            if data.get(checker).get("guild") is not None:
                descript = data.get(checker).get("guild").get("description")
                # object class Guild from guild.py
                guild = Guild_class(
                    description=descript,
                    name=data.get(checker).get("guild").get("name"))
            if data.get(checker).get("guild") is None:
                guild_name = None
            if Guild.objects.filter(name=guild.name).exists() is False:
                guild_name = Guild.objects.create(
                    name=guild.name,
                    description=guild.description)
            # object class Player from player.py
            player = Player_class(nickname=checker,
                                  email=data.get(checker).get("email"),
                                  bio=data.get(checker).get("bio"),
                                  race=race_hero,
                                  guild=guild_name)
            if Player.objects.filter(nickname=checker).exists() is False:
                Player.objects.create(
                    nickname=player.nickname,
                    email=player.email,
                    bio=player.bio,
                    race=player.race,
                    guild=player.guild)


def skills_update(skills: list, race_hero: callable) -> None:
    for skill in skills:
        # object class Skills from skills.py
        hero_skill = Skill_class(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race_hero)
        if Skill.objects.filter(
                name=hero_skill.name).exists() is False:
            Skill.objects.create(
                name=hero_skill.name,
                bonus=hero_skill.bonus,
                race=hero_skill.race)


if __name__ == "__main__":
    main()
