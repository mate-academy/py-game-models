import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"].get("description",
                                                             "")}
        )

        for skill_data in player_info["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        if player_info["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={
                    "description": player_info["guild"].get("description",
                                                            None)
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
