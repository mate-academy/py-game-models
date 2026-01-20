import json

import init_django_orm  # noqa: F401
from django.db import transaction
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # --- Read file players.json ---
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    with transaction.atomic():
        for player_name, player in data.items():
            # --- Race ---
            race_payload = player.get("race") or {}
            race_name = race_payload.get("name")
            race_desc = race_payload.get("description") or ""

            if not race_name:
                print(f"Player {player_name} skipped: missing race name.")
                raise ValueError("Missing race name")

            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_desc},
            )

            # --- Skills ---
            for sk in race_payload.get("skills") or []:
                skill_name = sk.get("name")
                skill_bonus = sk.get("bonus") or ""
                if not skill_name:
                    continue

                skill, _ = Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={"bonus": skill_bonus,
                              "race": race},
                )

            # --- Guild ---
            guild_payload = player.get("guild")
            guild = None
            if guild_payload:
                guild_name = guild_payload.get("name")
                guild_desc = guild_payload.get("description")

                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_desc},
                )

            # --- Player ---
            email = player.get("email")
            bio = player.get("bio") or ""

            Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": email,
                    "bio": bio,
                    "race": race,
                    "guild": guild,
                },
            )


if __name__ == "__main__":
    main()
