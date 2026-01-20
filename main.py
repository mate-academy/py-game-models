import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        data = json.load(json_file)
    for player_info, element in data.items():
        player, _ = Race.objects.get_or_create(
            name=element["race"]["name"],
            defaults={"description": element["race"]["description"]}
        )

        for power in element["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=power["name"],
                race=player,
                defaults={"bonus": power["bonus"]}
            )

        guild_info = element.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=element["guild"]["name"],
                defaults={
                    "description": element["guild"]["description"]
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_info,
            defaults={
                "email": element["email"],
                "bio": element["bio"],
                "race": player,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
