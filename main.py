import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        guild = None
        if player_data.get("guild"):
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }
        )

        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )


if __name__ == "__main__":
    main()
