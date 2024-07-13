import init_django_orm  # noqa: F401
import json
from django.utils import timezone
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        print(player_data)

        race_name = player_data["race"]["name"]
        race_description = player_data["race"].get("description", " ")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in player_data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data.get("description")
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
                "created_at": timezone.now()
            }
        )


if __name__ == "__main__":
    main()
