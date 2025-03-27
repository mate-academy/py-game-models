import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_info = player_data.get("race")
        race_player, created = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )
        skills = race_info.get("skills")
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race_player,
                bonus=skill.get("bonus"),
            )
        guild_info = player_data.get("guild")
        if guild_info:
            guild_player, created = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )
        else:
            guild_player = None
        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race_player,
            guild=guild_player
        )


if __name__ == "__main__":
    main()
