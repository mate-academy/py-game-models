import init_django_orm  # noqa: F401
import json
from django.db import transaction

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as f:
        player_data = json.load(f)

    with transaction.atomic():
        for player_name, data in player_data.items():

            race_data = data.get("race")

            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]},
            )

            for skill_data in race_data.get("skills", []):

                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )

            guild = None
            guild_data = data.get("guild")

            if guild_data is not None:

                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data["description"]}
                )

            player_mod, _ = Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": data["email"],
                    "bio": data["bio"],
                    "race": race,
                    "guild": guild,
                }
            )


if __name__ == "__main__":
    main()
