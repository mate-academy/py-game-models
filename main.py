import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as file:
        json_data = json.load(file)

    for user_name, user_data in json_data.items():
        # Race add:
        if Race.objects.filter(name=user_data["race"]["name"]).exists():
            race = Race.objects.get(name=user_data["race"]["name"])
        else:
            race = Race(
                name=user_data["race"]["name"],
                description=user_data["race"]["description"]
            )
            race.save()

        # Guild add:
        if user_data["guild"] is not None:
            if Guild.objects.filter(name=user_data["guild"]["name"]).exists():
                guild = Guild.objects.get(name=user_data["guild"]["name"])
            else:
                description = user_data["guild"]["description"]
                guild = Guild(
                    name=user_data["guild"]["name"],
                    description=description
                )
                guild.save()
        else:
            guild = None

        # Player add:
        Player.objects.create(
            nickname=user_name,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild,
        )

        # Skills add:
        for skill in user_data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                race_skill = Skill(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )
                race_skill.save()


if __name__ == "__main__":
    main()
