import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
        for name, user_data in data.items():
            player = Player(
                nickname=name,
                email=user_data["email"],
                bio=user_data["bio"],
            )

            race = Race.objects.get_or_create(
                name=user_data["race"]["name"],
                description=user_data["race"]["description"],
            )

            player.race = race[0]

            for skill in user_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race[0]
                )

            if user_data["guild"] is not None:
                guild = Guild.objects.get_or_create(
                    name=user_data["guild"]["name"],
                    description=user_data["guild"]["description"],
                )

                player.guild = guild[0]

            player.save()


if __name__ == "__main__":
    main()
