import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        guild_obj = None
        guild_info = player_data.get("guild")

        if guild_info:
            description_value = guild_info.get("description")

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": description_value}
            )

        race_info = player_data.get("race")

        if race_info:
            race_obj, _ = Race.objects.get_or_create(
                name=race_info.get("name"),
                defaults={"description": race_info.get("description", "")}
            )

            skills_list = race_info.get("skills", [])
            for skill_info in skills_list:
                Skill.objects.get_or_create(
                    name=skill_info.get("name"),
                    defaults={
                        "bonus": skill_info.get("bonus", ""),
                        "race": race_obj
                    }
                )

            email_value = player_data.get("email")
            bio_value = player_data.get("bio")

            if email_value and bio_value:
                Player.objects.create(
                    nickname=nickname,
                    email=email_value,
                    bio=bio_value,
                    race=race_obj,
                    guild=guild_obj
                )

    return Player.objects.all()


if __name__ == "__main__":
    main()
