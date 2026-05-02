import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player, info in data.items():
        race_dict = info.get("race")
        if race_dict:
            race_obj, race_created = Race.objects.get_or_create(
                name=race_dict.get("name"),
                defaults={"description": race_dict.get("description")},
            )

            skills_list = race_dict.get("skills")
            if skills_list:
                for skill in skills_list:
                    Skill.objects.get_or_create(
                        name=skill.get("name"),
                        defaults={
                            "bonus": skill.get("bonus"),
                            "race": race_obj,
                        }
                    )

        guilds_dict = info.get("guild")
        if guilds_dict:
            guild_obj, guild_created = Guild.objects.get_or_create(
                name=guilds_dict.get("name"),
                defaults={"description": guilds_dict.get("description")},
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race_obj if race_dict else None,
                "guild": guild_obj if guilds_dict else None
            }
        )


if __name__ == "__main__":
    main()
