import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main():
    with open("players.json", "r") as file:
        data = json.load(file)
        for player, info in data.items():
            if not Race.objects.filter(name=info["race"]["name"]).exists():
                race = Race.objects.create(
                    name=info["race"]["name"],
                    description=info["race"]["description"]
                )
            else:
                race = Race.objects.get(name=info["race"]["name"])
            for skill in info["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

            if info["guild"] is None:
                guild = None
            else:
                if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                    guild = Guild.objects.create(
                        name=info["guild"]["name"],
                        description=info["guild"]["description"]
                    )

            if not Player.objects.filter(nickname=player).exists():
                Player.objects.create(
                    nickname=player,
                    email=info["email"],
                    bio=info["bio"],
                    race=race,
                    guild=guild
                )


if __name__ == "__main__":
    main()
