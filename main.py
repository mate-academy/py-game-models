import json

import init_django_orm  # noqa: F401

from db.models import Race, Guild, Skill, Player # noqa


def get_or_create_race(race: dict) -> Race:
    obj, _ = Race.objects.get_or_create(
        name=race.get("name"),
        description=race.get("description")
    )
    return obj


def get_or_create_guild(guild: dict | None) -> Guild | None:
    if guild is None:
        return
    obj, _ = Guild.objects.get_or_create(
        name=guild.get("name"),
        description=guild.get("description")
    )
    return obj


def add_player(
        player: dict,
        nickname: str,
        race: Race,
        guild: Guild
) -> Player:
    obj, _ = race.player_set.get_or_create(
        nickname=nickname,
        email=player.get("email"),
        bio=player.get("bio"),
        guild=guild

    )
    return obj


def main() -> None:
    with open("players.json", "r") as players_file:
        data = json.load(players_file)
        for nickname, value in data.items():
            race_dict = value.get("race")
            race = get_or_create_race(race_dict)

            for skill_dict in race_dict.get("skills", []):
                race.skill_set.get_or_create(
                    name=skill_dict.get("name"),
                    bonus=skill_dict.get("bonus")
                )

            guild = get_or_create_guild(value.get("guild"))
            add_player(value, nickname, race, guild)


if __name__ == "__main__":
    main()
