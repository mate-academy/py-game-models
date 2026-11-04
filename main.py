# main.py
import os
import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "players.json")

    with open(json_path, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        player_skills_to_add = []
        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                }
            )
            player_skills_to_add.append(skill)

        guild = None
        if player_data.get("guild") is not None:
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )
        player.skills.set(player_skills_to_add)


if __name__ == "__main__":
    main()
