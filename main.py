import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        # Handle Race
        race_data = data.get("race")
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")}
        )

        # Handle Skills
        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race_obj
                }
            )

        # Handle Guild
        guild_obj = None
        guild_data = data.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        # Handle Player with get_or_create to avoid duplicates
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
