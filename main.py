import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_data in players.values():
        guild_data = player_data.get("guild")

        if guild_data:
            Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description"),
                },
            )

        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={"description": player_data["race"].get("description")}
        )

        for skill_data in player_data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={
                    "bonus": skill_data.get("bonus"),
                }
            )

    for player_name, player_data in players.items():
        race = Race.objects.get(name=player_data["race"]["name"])

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild = Guild.objects.get(name=guild_data.get("name"))

        bio = player_data.get("bio", "")

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email"),
                "race": race,
                "guild": guild,
                "bio": bio,
            }
        )


if __name__ == "__main__":
    main()
