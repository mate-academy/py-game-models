import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

        for nickname, info in data.items():
            race_obj, _ = Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            for skills_info in info["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skills_info["name"],
                    bonus=skills_info["bonus"],
                    race=race_obj
                )
            if info["guild"] is not None:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            else:
                guild_obj = None

            Player.objects.get_or_create(
                nickname=nickname,
                email=info["email"],
                bio=info["bio"],
                race=race_obj,
                guild=guild_obj
            )


if __name__ == "__main__":
    main()
