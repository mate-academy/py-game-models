import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data:
        players = json.load(data)

    for name, attribute in players.items():
        if not Race.objects.filter(name=attribute["race"]["name"]).exists():
            race_value = Race.objects.create(
                name=attribute["race"]["name"],
                description=attribute["race"]["description"]
            )
            for skill in attribute["race"]["skills"]:
                Skill.objects.create(name=skill["name"], bonus=skill["bonus"], race=race_value)
        else:
            race_value = Race.objects.get(name=attribute["race"]["name"])

        guild_value = None

        if attribute["guild"] is None:
            pass
        elif not Guild.objects.filter(name=attribute["guild"]["name"]).exists():
            guild_value = Guild.objects.create(
                name=attribute["guild"]["name"],
                description=attribute["guild"]["description"]
            )
        elif Guild.objects.filter(name=attribute["guild"]["name"]).exists():
            guild_value = Guild.objects.get(name=attribute["guild"]["name"])

        Player.objects.create(
            nickname=name,
            email=attribute["email"],
            bio=attribute["bio"],
            race=race_value,
            guild=guild_value,
        )


if __name__ == "__main__":
    main()

