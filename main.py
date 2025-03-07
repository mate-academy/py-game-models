import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

        for data, item in players_data.items():
            email = players_data[data]["email"]
            bio = players_data[data]["bio"]

            race_data = players_data[data]["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            for skill_info in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    defaults={"bonus": skill_info["bonus"]},
                    race=race
                )

            guild = None
            if players_data[data].get("guild"):
                guild_data = players_data[data]["guild"]
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            Player.objects.get_or_create(
                nickname=data,
                defaults={
                    "email": email,
                    "bio": bio,
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
