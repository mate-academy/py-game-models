import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Use get_or_create()
    # Read data
    print(Players.json.objects.all())


if __name__ == "__main__":
    main()
