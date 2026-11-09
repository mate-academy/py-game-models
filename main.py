import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players = json.load(f)

    for player, info in players.items():
        guild = None
        guild_info = info.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )

        race_info = info.get("race")
        if not race_info:
            print("A player without a race cannot be added.")
            continue
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={"description": race_info.get("description")}
        )
        for skill in race_info.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race,
                }
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
