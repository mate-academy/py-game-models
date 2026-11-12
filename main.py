import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for data, values in players_data.items():
        guild = None
        if values.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=values["guild"]["name"],
                description=values["guild"]["description"],
            )

        race, _ = Race.objects.get_or_create(
            name=values["race"]["name"],
            description=values["race"]["description"]
        )

        for skill in values["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.get_or_create(
            nickname=data,
            email=values["email"],
            bio=values["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
