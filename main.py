import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, data in players.items():
        race_data = data.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={"bonus": skill_data.get("bonus")}
            )

        guild = None
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
