import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        race_data = player_info.get("race", {})
        race_name = race_data.get("name")
        race_desc = race_data.get("description", "")
        skills_data = race_data.get("skills", [])

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc}
        )

        for skill_info in skills_data:
            skill_name = skill_info.get("name")
            skill_bonus = skill_info.get("bonus", "")
            Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race}
            )

        guild_data = player_info.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            guild_desc = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_desc}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info.get("email", ""),
                "bio": player_info.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
