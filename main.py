import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for key, item in players_data.items():

        race, _ = Race.objects.get_or_create(
            name=item["race"]["name"],
            description=item["race"]["description"]
        )

        for skill in item["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if item.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=item["guild"]["name"],
                description=item["guild"]["description"]
            )

        Player.objects.create(
            nickname=key,
            email=item["email"],
            bio=item["bio"],
            race=race,
            guild=guild if item.get("guild") else None
        )


if __name__ == "__main__":
    main()
