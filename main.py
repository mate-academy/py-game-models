import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

        for nickname, data in players.items():
            race, race_created = Race.objects.get_or_create(
                name=data["race"]["name"],
                defaults={
                    "description": data["race"]["description"]
                }
            )

            for skill in data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": race
                    }
                )

            if data["guild"] is not None:
                guild, guild_created = Guild.objects.get_or_create(
                    name=data["guild"]["name"],
                    defaults={
                        "description": data["guild"]["description"]
                    }
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": data["email"],
                    "bio": data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
