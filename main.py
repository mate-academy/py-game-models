import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        if isinstance(data, dict):
            data = data.get("players", [])

    for player_data in data:
        if isinstance(player_data, str):
            player_data = json.loads(player_data)
            
        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )

        guild = None
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
