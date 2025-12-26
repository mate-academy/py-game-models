import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race_players = player["race"]
        race, _ = Race.objects.get_or_create(
            name=race_players["name"],
            defaults={
                "description": race_players["description"]
                if "description" in race_players else None},
        )

        guild_players = player["guild"]
        if guild_players:
            guild, _ = Guild.objects.get_or_create(
                name=guild_players["name"],
                defaults={
                    "description": guild_players["description"]
                    if "description" in guild_players else None},
            )
        else:
            guild = None

        skills = player["race"]["skills"]
        for skill in skills:
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
