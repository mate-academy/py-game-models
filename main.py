import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_datails in players_data.items():
        race_data = player_datails["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data.get("bonus", 0),
                race=race,
            )

        guild_data = player_datails.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_datails["email"],
                "bio": player_datails.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
