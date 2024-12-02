import json
from tkinter.font import names

import init_django_orm  # noqa: F401
import json
from db.models import Guild, Race, Skill, Player


def main() -> None:
    with open("players.json", "r") as f:
        players_data=json.load(f)
    for player_data in players_data:
        race,_=Race.objects.get_or_create(name=player_data["race"]["name"],
                                            defaults={"description": player_data["race"].get("description", "")}
        )


        guild = None
        if "guild" in player_data and player_data["guild"]:
            guild,_=Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"].get("description", "")}
            )

        skills = []
        for skill_data in player_data.get("skills", []):
            skill,_=Skill.objects.get_or_create(name=skill_data["name"],
                                                defaults={"bonus": skill_data["bonus"], "race": race})
            skills.append(skill)

        Player.objects.get_or_create(nickname=player_data["nickname"],
                                     defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild,
            "created_at": player_data.get("created_at")
        })




if __name__ == "__main__":
    main()
