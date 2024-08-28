import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race_name = player_data["race"]["name"]
        race_description = player_data["race"].get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in player_data["race"].get("skills", []):
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_bonus}
            )
        guild_data = player_data.get("guild")
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data.get("description", "")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
