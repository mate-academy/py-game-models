import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        data = json.load(json_file)
        for element in data:
            player_info = data[element]
            player, _ = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                defaults={"description": player_info["race"]["description"]}
            )

            for power in player_info["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=power["name"],
                    race=player,
                    defaults={"bonus": power["bonus"]}
                )

            guild_info = player_info.get("guild")
            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=player_info["guild"]["name"],
                    defaults={
                        "description": player_info["guild"]["description"]
                    }
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=element,
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": player,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
