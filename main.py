import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json

def main() -> None:
    with open("players.json","r") as file:
        user_data = json.load(file)
        for player, data in user_data.items():

            race, _ = Race.objects.get_or_create(
                name=data.get("race", {}).get("name"),
                defaults={"description": data.get("race", {}).get("description")})

            guild = None
            if data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                     name=data.get("guild").get("name"),
                     defaults={"description": data.get("guild").get("description")}
                )
            if data.get("race", {}).get("skills", []) != []:
                for skill in data.get("race", {}).get("skills", []):
                    skill_details, _ = Skill.objects.get_or_create(
                        name=skill.get("name"),
                        defaults={"bonus": skill.get("bonus"),
                        "race": race})

            Player.objects.get_or_create(
                nickname=player,
                defaults={"email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild})


if __name__ == "__main__":
    main()