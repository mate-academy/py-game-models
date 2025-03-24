import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, stats in data.items():
        race, _ = Race.objects.get_or_create(
            name=stats["race"]["name"],
            description=stats["race"]["description"]
        )

        for skill in stats["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = stats.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=stats["guild"]["name"],
                description=stats["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=stats.get("email"),
            bio=stats.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
