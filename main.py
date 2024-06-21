import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json") as f:
        data = json.load(f)

    for nickname, info in data.items():
        email, bio, race_data, guild_data = info.values()

        race_instance, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_instance
            )

        if guild_data:
            guild_instance, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )
        else:
            guild_instance = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
