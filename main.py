import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for key, value in players.items():
        race_obj, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={"description": value["race"]["description"]}
        )

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_obj}
            )

        guild_data = value.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=key,
            defaults={
                "email": value["email"],
                "bio": value["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
