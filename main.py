import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        info_for_players = json.load(file)
    for name in info_for_players:
        race_info = info_for_players.get(name).get("race")
        race_object, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )
        skill_info = info_for_players.get(name).get("race").get("skills")
        for skill in skill_info:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_object)
        guild_info = info_for_players.get(name).get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=(
                    guild_info.get("description")
                )
            )
        else:
            guild = None
        Player.objects.create(
            nickname=name,
            email=info_for_players.get(name).get("email"),
            bio=info_for_players.get(name).get("bio"),
            race=race_object,
            guild=guild
        )


if __name__ == "__main__":
    main()
