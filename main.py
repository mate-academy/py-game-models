import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for player, data in players.items():
        race_info = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        skill_info = race_info["skills"]
        for skill in skill_info:
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = data["guild"]
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
