import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        data = json.load(json_file)
    for player_name, player_data in data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name")

        if not race_name:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_data.get("description", "")}
        )
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={"bonus": skill_data.get("bonus", "")}
            )
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")}
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
