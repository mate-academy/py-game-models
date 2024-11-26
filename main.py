import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, fields in data.items():
        if not Race.objects.filter(name=fields["race"]["name"]).exists():
            Race.objects.create(
                name=fields["race"]["name"],
                description=fields["race"]["description"],
            )

        race = Race.objects.get(name=fields["race"]["name"])

        for skill in fields["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        if fields["guild"]:
            if not Guild.objects.filter(name=fields["guild"]["name"]).exists():
                Guild.objects.create(
                    name=fields["guild"]["name"],
                    description=fields["guild"]["description"],
                )

            guild = Guild.objects.get(name=fields["guild"]["name"])

        else:
            guild = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=fields["email"],
                bio=fields["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
