import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        info_for_players = json.load(file)
    for name in info_for_players:
        race_info = info_for_players.get(name).get("race")
        Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )
        skill_info = info_for_players.get(name).get("race").get("skills")
        for skill in skill_info:
            race = Race.objects.get(
                name=race_info.get("name")
            )
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race)
        guild_info = info_for_players.get(name).get("guild")
        if guild_info is not None:
            Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=(
                    guild_info.get("description")
                )
            )
        Player.objects.create(
            nickname=name,
            email=info_for_players.get(name).get("email"),
            bio=info_for_players.get(name).get("bio"),
            race=Race.objects.get(
                name=race_info.get("name")
            ),
            guild=(
                Guild.objects.get(
                    name=guild_info.get("name")
                )
                if guild_info is not None
                else None
            )
        )


if __name__ == "__main__":
    main()
