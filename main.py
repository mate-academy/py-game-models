import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        data = json.load(players_file)

    for nickname, details in data.items():
        race_obj, _ = Race.objects.get_or_create(
            name=details["race"]["name"],
            defaults={"description": details["race"]["description"]}
        )

        for skill_detail in details["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_detail["name"],
                defaults={
                    "race": race_obj,
                    "bonus": skill_detail["bonus"],
                }
            )

        guild_obj = None
        if details.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=details["guild"]["name"],
                defaults={"description": details["guild"]["description"]}
            )

        Player.objects.update_or_create(
            nickname=nickname,
            defaults={
                "email": details["email"],
                "bio": details["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
