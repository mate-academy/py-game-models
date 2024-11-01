import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for player in players:
        player_data = players[player]

        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={
                "description": player_data["race"].get("description", "")
            }
        )

        skills = []
        for skill_data in player_data["race"].get("skills"):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )
            skills.append(skill)

        Player.objects.create(
            nickname=player,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=Guild.objects.get_or_create(
                **player_data.get("guild")
            )[0] if player_data.get("guild") else None
        )


if __name__ == "__main__":
    main()
