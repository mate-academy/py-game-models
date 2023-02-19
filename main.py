import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        players = json.load(data)
    for player, data in players.items():
        foreign_keys = {}
        if not Race.objects.filter(name=data["race"]["name"]).exists():
            race = Race(
                name=data["race"]["name"],
                description=data["race"]["description"],
            )
            race.save()
            foreign_keys["race"] = race
        else:
            foreign_keys["race"] = Race.objects.get(name=data["race"]["name"])
        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=foreign_keys["race"],
                )
        if (
            data.get("guild")
            and not Guild.objects.filter(
                name=data.get("guild").get("name")
            ).exists()
        ):
            guild = Guild(
                name=data["guild"]["name"],
                description=data["guild"]["description"],
            )
            guild.save()
            foreign_keys["guild"] = guild
        elif data.get("guild"):
            foreign_keys["guild"] = Guild.objects.get(
                name=data["guild"]["name"]
            )
        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=foreign_keys.get("race"),
            guild=foreign_keys.get("guild"),
        )


if __name__ == "__main__":
    main()
