import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for nickname, info in players_data.items():
        race = info["race"]
        race_to_add, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        for skill in race["skills"]:
            Skill.objects.get_or_create(
                race=race_to_add,
                name=skill["name"],
                bonus=skill["bonus"]
            )

        guild = info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_to_add,
            guild=guild)


if __name__ == "__main__":
    main()
