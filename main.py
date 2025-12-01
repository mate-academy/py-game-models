import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as file:
        json_players = json.load(file)
        for nickname, data in json_players.items():
            race, _ = Race.objects.get_or_create(
                name=data["race"]["name"],
                defaults={"description": data["race"].get("description", "")},
            )

            for skill_data in data["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data.get("bonus", "")},
                )

            guild = None
            if data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=data["guild"]["name"],
                    defaults={"description": data["guild"].get("description")},
                )

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": data["email"],
                    "bio": data.get("bio", ""),
                    "race": race,
                    "guild": guild,
                },
            )


if __name__ == "__main__":
    main()
