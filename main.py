import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    # jeśli JSON to dict {nickname: {...}}, iterujemy po items()
    if isinstance(players_data, dict):
        players_iter = players_data.items()
    else:  # jeśli JSON to list [{...}, {...}]
        players_iter = [(p["nickname"], p) for p in players_data]

    for nickname, pdata in players_iter:
        # --- Race ---
        race_data = pdata["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        # --- Guild ---
        guild_obj = None
        if pdata.get("guild"):
            guild_data = pdata["guild"]
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        # --- Skills ---
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )

        # --- Player ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata.get("email", ""),
                "bio": pdata.get("bio", ""),
                "race": race,
                "guild": guild_obj,
            },
        )
