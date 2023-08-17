import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, data in players.items():
        race_data = data["race"]
        race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"])[0]

        skills_data = race_data["skills"]
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = data["guild"]
        if guild:
            guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        player_query = Player.objects.filter(nickname=player)
        if not player_query.exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
