import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json") as file:
        context = json.load(file)
    for player, information in context.items():

        # створюємо гільдії
        guild = None
        if information["guild"]:
            guild = Guild.objects.get_or_create(
                name=information["guild"]["name"],
                description=information["guild"]["description"],
            )

        # створюємо раси
        Race.objects.get_or_create(
            name=information["race"]["name"],
            description=information["race"]["description"],
        )

        # створюємо скіли
        race = Race.objects.get(name=information["race"]["name"])
        if information["race"]["skills"]:
            for skills in information["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=race
                )

        # створюємо гравця
        if guild is not None:
            guild = Guild.objects.get(name=information["guild"]["name"])
        Player.objects.get_or_create(
            nickname=player,
            email=information["email"],
            bio=information["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
