import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        guild = player_data["guild"]
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )
        guild = Guild.objects.get(name=guild["name"]) if guild else None

        race_dict = player_data["race"]
        if not Race.objects.filter(name=race_dict["name"]).exists():
            Race.objects.create(
                name=race_dict["name"],
                description=race_dict["description"]
            )
        race = Race.objects.get(name=race_dict["name"])

        for skill in race_dict["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
