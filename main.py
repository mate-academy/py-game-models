import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race_instance(race_info: dict) -> Race:
    race_instance, _ = Race.objects.get_or_create(
        name=race_info["name"],
        description=race_info["description"]
    )
    return race_instance


def create_guild_instance(guild_info: dict) -> Guild:
    guild_instance, _ = Guild.objects.get_or_create(**guild_info)
    return guild_instance


def create_skill_fields(skills_info: list, race: Race) -> None:
    for skill in skills_info:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def main() -> None:
    with open("players.json") as players_source:
        players_info = json.load(players_source)
    for player in players_info:
        race = create_race_instance(players_info[player]["race"])
        guild = create_guild_instance(players_info[player]["guild"])\
            if players_info[player]["guild"] else None
        Player.objects.create(
            nickname=player,
            email=players_info[player]["email"],
            bio=players_info[player]["bio"],
            race=race,
            guild=guild
        )
        create_skill_fields(players_info[player]["race"]["skills"], race)


if __name__ == "__main__":
    main()
