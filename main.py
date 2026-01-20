import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for player_name in players_data:
        player_data = players_data[player_name]
        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"]["description"]},
        )

        guild = player_data.get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={
                    "description": player_data["guild"].get("description")
                },
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )


if __name__ == "__main__":
    main()
