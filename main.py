import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for nickname, info in players.items():
        race_data = info.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")}
        )
        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race,
                defaults={"bonus": skill.get("bonus")}
            )
        guild_data = info.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
