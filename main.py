import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild
from django.db.utils import IntegrityError


def main() -> None:
    with open("./players.json") as file:
        context = json.load(file)
    for player, information in context.items():

        # створюємо гільдії
        guild = None
        if information["guild"]:
            guild = Guild(
                name=information["guild"]["name"],
                description=information["guild"]["description"],
            )
            try:
                guild.save()
            except IntegrityError:
                pass

        # створюємо раси
        race = Race(
            name=information["race"]["name"],
            description=information["race"]["description"],
        )
        try:
            race.save()
        except IntegrityError:
            pass

        # створюємо скіли
        race = Race.objects.get(name=race.name)

        if information["race"]["skills"]:
            for skills in information["race"]["skills"]:
                skill = Skill(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=race
                )
                try:
                    skill.save()
                except IntegrityError:
                    pass

        # створюємо гравця
        race = Race.objects.get(name=race.name)
        if guild is not None:
            guild = Guild.objects.get(name=guild.name)
        person = Player(
            nickname=player,
            email=information["email"],
            bio=information["bio"],
            race=race,
            guild=guild,
        )

        try:
            person.save()
        except IntegrityError:
            pass


if __name__ == "__main__":
    main()
