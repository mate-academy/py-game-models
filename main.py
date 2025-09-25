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
        RACE = Race.objects.get_or_create(
            name=p_value["race"]["name"],
            description=p_value["race"]["description"]
        )[0]

        for skill in p_value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=RACE
            )

        guild = Guild.objects.get_or_create(
            name=p_value["guild"]["name"],
            description=p_value["guild"]["description"]
        )[0] if p_value["guild"] else None

        Player.objects.create(
            nickname=player,
            email=p_value["email"],
            bio=p_value["bio"],
            race=RACE,
            guild=guild
        )


if __name__ == "__main__":
    main()
