import init_django_orm  # noqa: F401
import json
from django.db import transaction

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for player_name, player_data in data.items():
        with transaction.atomic():
            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")},
            )
            for skill_data in race_data["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]},
                )

            guild_data = player_data.get("guild")
            guild_defaults = (
                {
                    "description": guild_data.get("description")
                } if guild_data else {}
            )
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data.get("name", ""), defaults=guild_defaults
                )

            player_defaults = {
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
            player, _ = Player.objects.get_or_create(
                nickname=player_name, defaults=player_defaults
            )


if __name__ == "__main__":
    main()
