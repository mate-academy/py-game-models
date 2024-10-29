import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        users = json.loads(file.read())
        for nickname, params in users.items():
            params_race = params["race"]
            race, _ = Race.objects.get_or_create(
                name=params_race["name"],
                description=params_race["description"]
            )
            params_gild = params["guild"]
            if params_gild:
                guild, _ = Guild.objects.get_or_create(
                    name=params_gild["name"],
                    description=params_gild.get("description", "")
                )
            else:
                guild = None
            skills = []
            for skill in params_race["skills"]:
                skill_obj, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    race=race,
                    bonus=skill.get("bonus", "")
                )
                skills.append(skill_obj)

            Player.objects.create(
                nickname=nickname,
                email=params["email"],
                bio=params["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
