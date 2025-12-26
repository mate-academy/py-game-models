import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_dict = json.load(f)

    for nickname, player_data in players_dict.items():
        race_info = player_data.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={"description": race_info.get("description", "")}
        )

        guild_info = player_data.get("guild")
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )

        for skill_data in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={"bonus": skill_data.get("bonus", "")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
