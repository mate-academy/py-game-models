import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_data:
        players = json.load(player_data)
    for player_name, player_contents in players.items():
        guild_data = player_contents.get("guild")
        guild = None
        if guild_data:  # Will be False if guild_data is None
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )
        Player.objects.create(
            nickname=player_name,
            email=player_contents.get("email"),
            bio=player_contents.get("bio"),
            race=Race.objects.get_or_create(
                name=player_contents.get("race", {}).get("name"),
                description=player_contents.get("race", {}).get("description"),
            )[0],
            guild=guild
        )
        for skill in player_contents.get("race", {}).get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=Race.objects.get_or_create(
                    name=player_contents.get("race", {}).get("name"),
                    description=player_contents.get(
                        "race", {}
                    ).get("description")
                )[0]
            )


if __name__ == "__main__":
    main()
