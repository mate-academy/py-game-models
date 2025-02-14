import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for player, description in data.items():
        race, is_created = Race.objects.get_or_create(
            name=description["race"]["name"],
            description=description["race"]["description"],
        )

        if is_created:
            skills = description["race"]["skills"]
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        guild_data = description.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description"),
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=description["email"],
            bio=description["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
