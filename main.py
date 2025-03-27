import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")
        skill_data = race_data.get("skills")

        race_data, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        for skill in skill_data:
            skill = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_data
            )

        if guild_data:
            guild_data, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_data,
            guild=guild_data
        )


if __name__ == "__main__":
    main()
