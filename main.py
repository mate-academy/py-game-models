import json

import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for name, data in players.items():

        player = Player(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
        )

        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"],
        )

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"],
            )
            player.guild = guild

        player.race = race
        player.save()


if __name__ == "__main__":
    main()
