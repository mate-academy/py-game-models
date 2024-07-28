import init_django_orm  # noqa: F401

from typing import Optional, Any
from django.db.models import QuerySet
from db.models import Actor, Genre, Guild


def create_guild(guild_info: Optional[dict[str, Any]]) -> Optional[Guild]:
    if guild_info:
        guild, _ = Guild.objects.get_or_create(
            name=guild_info["name"],
            description=guild_info["description"]
        )
        return guild
    return None


def main() -> QuerySet:
    genres = [
        "Western",
        "Action",
        "Dramma",
    ]
    for genre in genres:
        Genre.objects.create(name=genre)

    actors = [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").all().order_by("first_name")


if __name__ == "__main__":
    main()
