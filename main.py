import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    data = json.load(open('players.json'))
    for i, j in data.items():
        print(i)
        print(j)

    first_user = next(iter(data))
    print("DATA:", data[first_user])

    Player.objects.get_or_create(
        nickname=first_user,
        email=data[first_user]['email'],
        bio=data[first_user]['bio'],
        race=None,
    )

    Race.objects.get_or_create(
        name=data[first_user]['race']['name'],
        description=data[first_user]['race']['description'],
    )



if __name__ == "__main__":
    main()
