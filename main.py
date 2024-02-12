import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def load_players_from_file(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)


def main() -> None:
    players = load_players_from_file("players.json")

    for player, data in players.items():
        race, was_created = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        if was_created:
            if "skills" in data["race"]:
                for skill in data["race"]["skills"]:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        guild = data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(**guild)

        Player.objects.create(
            nickname=player,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
