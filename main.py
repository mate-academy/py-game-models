import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    # json_path = os.path.join(base_dir, "players.json")

    with open("players.json", "r") as f:
        players_data = json.load(f)

    for player_data in players_data:
        if not isinstance(player_data, dict):
            continue

        guild_info = player_data.get("guild")
        guild = None
        if isinstance(guild_info, dict):
            guild_name = guild_info.get("name")
            guild_desc = guild_info.get("description")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_desc}
                )

        race_info = player_data.get("race")
        race = None
        if isinstance(race_info, dict):
            race_name = race_info.get("name")
            race_desc = race_info.get("description")
            if race_name:
                race, _ = Race.objects.get_or_create(
                    name=["race_name"],
                    defaults={"description": race_desc}
                )

        player = Player.objects.create(
            nickname=player_data.get("nickname", "Unknown"),
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            guild=guild,
            race=race
        )

        skills_info = player_data.get("skills", [])
        if isinstance(skills_info, list):
            for skill_info in skills_info:
                if isinstance(skill_info, dict):
                    skill_name = skill_info.get("name")
                    skill_bonus = skill_info.get("bonus")
                    if skill_name:
                        skill, _ = Skill.objects.get_or_create(
                            name=skill_name,
                            defaults={"bonus": skill_bonus}
                        )


if __name__ == "__main__":
    main()
