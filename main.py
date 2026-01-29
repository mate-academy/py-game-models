import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nick, info in data.items():
        player = Player.objects.get_or_create(
            nickname=nick,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get_or_create(
                name=info["race"]["name"],
                defaults={
                    "description": info["race"].get("description")
                }
            )[0]
        )[0]

        if info["race"].get("skills"):
            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": player.race
                    }
                )

        if info.get("guild"):
            player.guild = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                defaults={
                    "description": info["guild"].get("description")
                }
            )[0]

        player.save()


if __name__ == "__main__":
    main()
