import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_characters = open("players.json")
    data = json.load(file_characters)
    for player in data:
        race_name = data.get(player).get("race").get("name")
        race_descript = data.get(player).get("race").get("description")
        race_hero = race_update(race_name, race_descript)
        skills = data.get(player).get("race").get("skills")
        skill_update(skills, race_hero)
        guild_check = data.get(player).get("guild")
        guild = guild_update(guild_check)
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data.get(player).get("email"),
                bio=data.get(player).get("bio"),
                race=race_hero,
                guild=guild)
    file_characters.close()


def race_update(race_name: str, race_description: str) -> Race.objects:
    if not Race.objects.filter(name=race_name).exists():
        return Race.objects.create(
            name=race_name,
            description=race_description)
    else:
        return Race.objects.filter(name=race_name).get()


def skill_update(skills: list, race: Race.objects) -> None:
    for skill in skills:
        if not Skill.objects.filter(
                name=skill.get("name")).exists():
            Skill.objects.create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race)


def guild_update(guild: [dict, None]) -> Guild.objects:
    if guild is not None:
        if not Guild.objects.filter(
                name=guild.get("name")).exists():
            return Guild.objects.create(
                name=guild.get("name"),
                description=guild.get("description"))
    if guild is None:
        return None
    else:
        return Guild.objects.filter(
            name=guild.get("name")).get()


if __name__ == "__main__":
    main()
