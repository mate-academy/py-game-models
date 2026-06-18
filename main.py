import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        if not isinstance(player_data, dict):
            continue

        race_data = player_data.get("race")
        if not race_data or not isinstance(race_data, dict):
            continue

        race_name = race_data.get("name")
        if not race_name:
            continue

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_data.get("description", "")}
        )

        skills_list = race_data.get("skills", [])
        if isinstance(skills_list, list):
            for skill_item in skills_list:
                if isinstance(skill_item, dict):
                    skill_name = skill_item.get("name")
                    if skill_name:
                        Skill.objects.get_or_create(
                            name=skill_name,
                            race=race_obj,
                            defaults={"bonus": skill_item.get("bonus", "")}
                        )

        guild_data = player_data.get("guild")
        guild_obj = None
        if guild_data and isinstance(guild_data, dict):
            guild_name = guild_data.get("name")
            if guild_name:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_data.get("description")}
                )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    import init_django_orm  # noqa: F401
    main()
