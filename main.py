import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        info = json.load(file)

    for player_nickname, player_info in info.items():
        race = create_race(player_info)
        guild = create_guild(player_info)

        Player.objects.create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )

        create_skills(player_info)


def create_race(player_info: dict) -> Race:
    if not Race.objects.filter(name=player_info["race"]["name"]).exists():
        return Race.objects.create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

    return Race.objects.get(name=player_info["race"]["name"])


def create_guild(player_info: dict) -> Guild | None:
    if player_info["guild"]:
        if not Guild.objects.filter(
                name=player_info["guild"]["name"]
        ).exists():
            return Guild.objects.create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )

        return Guild.objects.get(name=player_info["guild"]["name"])
    return None


def create_skills(player_info: dict) -> None:
    for skill in player_info["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=create_race(player_info)
            )


if __name__ == "__main__":
    main()
