import os
import json
from django.utils import timezone
from db.models import Race, Skill, Guild, Player


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "players.json")

    with open(json_path, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for player_key, pdata in players_data.items():
        nickname = player_key  # ключ словника використаємо як nickname

        # --- Race ---
        race_data = pdata.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", ""),
            defaults={"description": race_data.get("description", "")}
        )

        # --- Guild ---
        guild = None
        if pdata.get("guild"):
            guild_data = pdata["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", ""),
                defaults={"description": guild_data.get("description", "")}
            )

        # --- Player ---
        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata.get("email", ""),
                "bio": pdata.get("bio", ""),
                "race": race,
                "guild": guild,
                "created_at": timezone.now()
            }
        )

        # --- Skills ---
        for sdata in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=sdata.get("name", ""),
                race=race,
                defaults={"bonus": sdata.get("bonus", 0)}
            )


if __name__ == "__main__":
    main()
