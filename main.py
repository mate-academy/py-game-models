import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        race_obj, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"]["description"]}
        )

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race_obj,
                defaults={"bonus": skill["bonus"]}
            )

        guild_obj = None
        if data.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
