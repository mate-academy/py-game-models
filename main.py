import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        players = json.load(player_file)
    for nickname, player_info in players.items():
        guild = player_info.get("guild")
        guild_obj = None
        if guild is not None:
            guild_obj, is_created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        race = player_info.get("race")
        race_obj, is_created = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )
        for skill in race.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_obj
            )
        Player.objects.create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
