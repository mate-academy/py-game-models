import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for nickname, info in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"],
        )
        guild = None
        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"],
            )
        for skill in info["race"].get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        Player.objects.get_or_create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
