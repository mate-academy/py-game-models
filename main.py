import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name")
        if race_name:
            race, created = Race.objects.get_or_create(
                name=race_name,
                description=race_data.get("description", "")
            )

            skills_data = race_data.get("skills", [])

            for skill_data in skills_data:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )

        guild_data = player_data.get("guild", {})
        guild_name = guild_data.get("name") if guild_data else None

        if guild_name:
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_data.get("description", "")
            )

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild if guild_name else None
        )

if __name__ == "__main__":
    main()
