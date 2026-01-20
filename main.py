import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_info in players_data.items():
        race_data = player_info.get("race")
        race_obj = None
        if race_data:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")},
            )
            skills_list = race_data.get("skills")
            if skills_list:
                for skill_data in skills_list:
                    Skill.objects.get_or_create(
                        name=skill_data["name"],
                        defaults={
                            "bonus": skill_data["bonus"],
                            "race": race_obj}
                    )

        guild_data = player_info.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )
        if race_obj:
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": race_obj,
                    "guild": guild_obj,
                },
            )


if __name__ == "__main__":
    main()
