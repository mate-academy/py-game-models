import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, info in players.items():

        current_email = info["email"]
        current_bio = info["bio"]
        current_race = info["race"]
        current_guild = info["guild"]
        current_skills = current_race["skills"]

        if not Race.objects.filter(name=current_race["name"]).exists():
            Race.objects.create(
                name=current_race["name"],
                description=current_race["description"]
            )
        current_race = Race.objects.get(name=current_race["name"])

        if current_guild:
            if not Guild.objects.filter(name=current_guild["name"]).exists():
                Guild.objects.create(
                    name=current_guild["name"],
                    description=current_guild["description"]
                )
            current_guild = Guild.objects.get(name=current_guild["name"])

        if current_skills:
            for skill in current_skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=current_race,
                    )

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=current_email,
                bio=current_bio,
                race=current_race,
                guild=current_guild,
            )


if __name__ == "__main__":
    main()
