import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "r") as players:
        data = json.load(players)
        for (name, value) in data.items():
            race, _ = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"],
            )
            for skill in value["race"]["skills"]:
                get_skill, _ =  Skill.objects.get_or_create(
                    name=skill["name"], bonus=skill["bonus"], race=race
                )

            if value['guild']:
                print(name, value['guild'])
                guild, _ = Guild.objects.get_or_create(
                    name=value['guild']['name']
                )
                if value["guild"]["description"]:
                    guild.description = value["guild"]["description"]
                    guild.save()
            else:
                guild = None;

            Player.objects.get_or_create(
                nickname=name,
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild,
            )

if __name__ == "__main__":
    main()
