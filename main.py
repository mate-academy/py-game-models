import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as json_file:
        players_dict = json.load(json_file)

    for nickname, info in players_dict.items():
        try:
            race = Race.objects.get(name=info["race"]["name"])
        except Race.DoesNotExist:
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

        player = Player.objects.create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race
        )

        if info.get("guild"):
            try:
                guild = Guild.objects.get(name=info["guild"]["name"])
            except Guild.DoesNotExist:
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"].get("description")
                )
            player.guild = guild
            player.save()

        for skill in info["race"]["skills"]:
            try:
                Skill.objects.get(name=skill["name"], race=race)
            except Skill.DoesNotExist:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
