import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        data = json.load(file)
        print(data)

    for player in data:
        if not Race.objects.filter(name=data[player]["race"]["name"]).exists():
            Race.objects.create(
                name=data[player]["race"]["name"],
                description=data[player]["race"]["description"]
            )

        if data[player]["guild"]:
            if not Guild.objects.filter(name=data[player]["guild"]["name"]) \
                    .exists():
                Guild.objects.create(
                    name=data[player]["guild"]["name"],
                    description=data[player]["guild"]["description"]
                )

        for skill in data[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects
                    .get(name=f'{data[player]["race"]["name"]}')
                )

        new_player = Player.objects.create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=Race.objects.get(name=f'{data[player]["race"]["name"]}'))
        if data[player]["guild"]:
            new_player.guild = Guild.objects\
                .get(name=data[player]["guild"]["name"])
            new_player.save()


if __name__ == "__main__":
    main()
