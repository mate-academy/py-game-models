import json
import logging

import init_django_orm  # noqa: F401
from django.db import transaction

from db.models import Race, Skill, Player, Guild

logging.basicConfig(level=logging.INFO)


def main() -> None:
    try:
        with open("players.json", "r") as file:
            players_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error(f"Error loading JSON: {error}")
        return

    for nickname, data in players_data.items():
        try:
            with transaction.atomic():
                race_data = data.get("race")
                race, _ = Race.objects.get_or_create(
                    name=race_data.get("name"),
                    defaults={"description": race_data.get("description", "")}
                )

                for skill_data in race_data.get("skills", []):
                    Skill.objects.get_or_create(
                        name=skill_data.get("name"),
                        race=race,
                        defaults={"bonus": skill_data.get("bonus")}
                    )

                guild = None
                guild_data = data.get("guild")
                if guild_data:
                    guild, _ = Guild.objects.get_or_create(
                        name=guild_data.get("name"),
                        defaults={"description": guild_data.get("description")}
                    )

                Player.objects.update_or_create(
                    nickname=nickname,
                    defaults={
                        "email": data.get("email"),
                        "bio": data.get("bio"),
                        "race": race,
                        "guild": guild,
                    }
                )

        except Exception as e:
            logging.error(f"Error processing player {nickname}: {e}")
            continue


if __name__ == "__main__":
    main()
