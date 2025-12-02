import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    # Wczytanie JSON
    with open("players.json", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, pdata in players_data.items():

        # --- RACE ---
        race_info = pdata["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")},
        )

        # --- GUILD ---
        guild_info = pdata.get("guild")
        guild_obj = None

        if guild_info is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")},
            )

        # --- SKILLS ---
        for skil in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skil["name"],
                race=race,
                defaults={"bonus": skil["bonus"]},
            )

        # --- PLAYER ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
