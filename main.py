import json
import init_django_orm  # noqa: F401

from django.utils.timezone import now
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

        for nickname, player in players_data.items():
            race_data = player["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]}
                )

            guild = None
            guild_data = player.get("guild")
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")}
                )

            Player.objects.update_or_create(
                nickname=nickname,
                defaults={
                    "email": player.get("email", ""),
                    "bio": player.get("bio", ""),
                    "race": race,
                    "guild": guild,
                }
            )


if __name__ == "__main__":
    main()
