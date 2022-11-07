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
            if not Race.objects.filter(name=race.name).exists():
                race_hero = Race.objects.create(name=race.name,
                                                description=race.description)
            skills = data.get(checker).get("race").get("skills")
            skills_update(skills, race_hero)
            if not data.get(checker).get("guild") is None:
                guild_name = guild_update(data, checker)
            if data.get(checker).get("guild") is None:
                guild_name = None
            # object class Player from player.py
            player = Player_class(nickname=checker,
                                  email=data.get(checker).get("email"),
                                  bio=data.get(checker).get("bio"),
                                  race=race_hero,
                                  guild=guild_name)
            if not Player.objects.filter(nickname=checker).exists():
                Player.objects.create(
                    nickname=player.nickname,
                    email=player.email,
                    bio=player.bio,
                    race=player.race,
                    guild=player.guild)


def guild_update(players_data, player_check) -> [str, None]:
    descript = players_data.get(player_check).get("guild").get("description")
    # object class Guild from guild.py
    guild = Guild_class(
        description=descript,
        name=players_data.get(player_check).get("guild").get("name"))
    if not Guild.objects.filter(name=guild.name).exists():
        return Guild.objects.create(
            name=guild.name,
            description=guild.description)


def skills_update(skills: list, race_hero: callable) -> None:
    for skill in skills:
        # object class Skills from skills.py
        hero_skill = Skill_class(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race_hero)
        if not Skill.objects.filter(
                name=hero_skill.name).exists():
            Skill.objects.create(
                name=hero_skill.name,
                bonus=hero_skill.bonus,
                race=hero_skill.race)


if __name__ == "__main__":
    main()
