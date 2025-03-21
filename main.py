import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_name = player_data["race"]["name"]
        race_description = player_data["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

            guild_data = player_data["guild"]
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")}
                )

            Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
