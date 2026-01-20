import json
import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_path = "./players.json"

    with open(file_path, "r") as file:
        data = json.load(file)

        for player, info in data.items():
            race_data = info["race"]
            race_instance, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            guild_info = info["guild"]
            if guild_info and guild_info.get("name"):
                 guild_instance, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description")}
                )

            skills_info = race_data["skills"]
            for skill in skills_info:
                if skill and skill.get("name"):
                     skill_instance, _ = Skill.objects.get_or_create(
                        name=skill["name"],
                        race=race_instance,
                        defaults={"bonus": skill.get("bonus")}
                    )

            Player.objects.create(
                nickname=player,
                email=info["email"],
                bio=info["bio"],
                guild=guild_instance,
                race=race_instance,
            )


if __name__ == "__main__":
    main()
