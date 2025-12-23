import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as read_file:
        players = json.load(read_file)
    for name, info in players.items():
        race_obj, _ = Race.objects.get_or_create(
            name=info.get("race").get("name"),
            description=info.get("race").get("description")
        )

        guild_data = info.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        player_obj, _ = Player.objects.get_or_create(
            nickname=name,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_obj,
            guild=guild_obj
        )

        for skill in info.get("race").get("skills"):
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_obj
            )


if __name__ == "__main__":
    main()
