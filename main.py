import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as file:
        content = json.load(file)

    for name_player, info in content.items():
        race = Race.objects.filter(name=info["race"]["name"])

        if not race:
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        else:
            race = Race.objects.get(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

        for title, val in info["race"].items():
            if title == "skills" and val:
                for item in val:
                    skill = Skill.objects.filter(name=item["name"])
                    if not skill:
                        Skill.objects.create(
                            name=item["name"],
                            bonus=item["bonus"],
                            race_id=race.id
                        )
        if not info["guild"]:
            guild = None
        else:
            guild = Guild.objects.filter(name=info["guild"]["name"])
            if not guild:
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                ).id
            else:
                guild = Guild.objects.get(name=info["guild"]["name"]).id

        player = Player.objects.filter(nickname=name_player)
        if not player:
            Player.objects.create(
                nickname=name_player,
                email=info["email"],
                bio=info["bio"],
                race_id=race.id,
                guild_id=guild
            )


if __name__ == "__main__":
    main()
