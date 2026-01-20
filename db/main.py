from db.models import Race, Skill, Guild, Player

import json


def main() -> None:

    with open("player.json", "r") as file:
        data = json.load(file)

    for nickname, details in data.items():

        race_data = details.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")}
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        guild = None
        guild_data = details.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": details["email"],
                "bio": details["bio"],
                "race": race,
                "guild": guild
            }
        )
