import json
from typing import Union

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def create_race(name: str, description: str) -> Race:
    race, _ = Race.objects.get_or_create(
        name=name,
        defaults={"description": description}
    )
    return race


def create_guild(guild_data: dict) -> Union[Guild, None]:
    if guild_data:
        return Guild.objects.get_or_create(
            name=guild_data.get("name"),
            defaults={"description": guild_data.get("description")}
        )[0]
    return None


def create_player(
        nickname: str,
        player_data: dict,
        race: Race,
        guild: Guild
) -> None:
    Player.objects.get_or_create(
        nickname=nickname,
        defaults={
            "email": player_data.get("email"),
            "bio": player_data.get("bio"),
            "race": race,
            "guild": guild,
        }
    )


def create_skills(race: Race, skills: list) -> None:
    for skill_data in skills:
        Skill.objects.get_or_create(
            name=skill_data.get("name"),
            defaults={
                "bonus": skill_data.get("bonus"),
                "race": race,
            }
        )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race = create_race(
            name=player.get("race").get("name"),
            description=player.get("race").get("description")
        )

        guild = create_guild(player.get("guild"))

        create_player(nickname, player, race, guild)

        create_skills(race, player["race"].get("skills", []))


if __name__ == "__main__":
    main()
