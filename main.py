import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_or_create_race(race: dict) -> Race:
    obj, _ = Race.objects.get_or_create(
        name=race.get("name"),
        description=race.get("description")
    )
    obj.save()
    return obj


def get_or_create_skill(skill: dict, race: Race) -> Skill:
    obj, _ = Skill.objects.get_or_create(
        name=skill.get("name"),
        bonus=skill.get("bonus"),
        race=race
    )
    obj.save()
    return obj


def get_or_create_guild(guild: dict | None) -> Guild | None:
    if guild is None:
        return
    obj, _ = Guild.objects.get_or_create(
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
) -> None:
    obj, _ = Player.objects.get_or_create(
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
