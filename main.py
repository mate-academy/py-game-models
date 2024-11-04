import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_or_create_race(race: dict) -> Race:
    try:
        obj = Race.objects.get(name=race.get("name"))
        return obj
    except Race.DoesNotExist:
        obj = Race.objects.create(
            name=race.get("name"),
            description=race.get("description")
        )
        obj.save()
        return obj


def get_or_create_skill(skill: dict, race: Race) -> Skill:
    try:
        obj = Skill.objects.get(name=skill.get("name"))
        return obj
    except Skill.DoesNotExist:
        obj = Skill.objects.create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race
        )
        obj.save()
        return obj


def get_or_create_guild(guild: dict | None) -> Guild | None:
    if guild is None:
        return
    try:
        obj = Guild.objects.get(name=guild.get("name"))
        return obj
    except Guild.DoesNotExist:
        obj = Guild.objects.create(
            name=guild.get("name"),
            description=guild.get("description")
        )
        obj.save()
        return obj


def add_player(
        player: dict,
        nickname: str,
        race: Race,
        guild: Guild
) -> Player:
    try:
        obj = Player.objects.get(nickname=player.get("name"))
        return obj
    except Player.DoesNotExist:
        obj = Player.objects.create(
            nickname=nickname,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild

        )
        obj.save()


def main() -> None:
    data = json.load(open("players.json", "r"))

    for nickname, value in data.items():
        race_dict = value.get("race")
        race = get_or_create_race(race_dict)

        for skill_dict in race_dict.get("skills"):
            get_or_create_skill(skill_dict, race)

        guild = get_or_create_guild(value.get("guild"))
        add_player(value, nickname, race, guild)


if __name__ == "__main__":
    main()
