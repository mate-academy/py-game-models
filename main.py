import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race = player.get("race")
        race_obj, created = Race.objects.get_or_create(
            name=race.get("name"),
            defaults={
                "description": race.get("description")
            }
        )
        for skill in race.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race_obj
                }
            )
        guild = player.get("guild")
        if guild:
            guild_obj, created = Guild.objects.get_or_create(
                name=guild.get("name"),
                defaults={
                    "description": guild.get("description")
                }
            )
        else:
            guild_obj = None
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player.get("email"),
                "bio": player.get("bio"),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
