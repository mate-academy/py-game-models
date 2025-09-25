import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json", "r") as file:
        data = json.load(file)
    for player, p_value in data.items():
        Race.objects.get_or_create(
            name=p_value["race"]["name"],
            description=p_value["race"]["description"]
        )

        RACE = Race.objects.get(name=p_value["race"]["name"])

        for skill in p_value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=RACE
            )

        guild = p_value.get("guild")
        if guild:
            Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.create(
            nickname=player,
            email=p_value["email"],
            bio=p_value["bio"],
            race=RACE,
            guild=Guild.objects.get(name=guild["name"]) if guild else None
        )


if __name__ == "__main__":
    main()
