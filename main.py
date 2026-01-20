import json
from db.models import Race, Skill, Guild, Player
from django.db import transaction


def main() -> str:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    with transaction.atomic():
        for nickname, player_data in players_data.items():
            race_info = player_data.get("race", {})
            race_name = race_info.get("name")
            race_description = race_info.get("description", "")
            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description}
            )

            for skill_data in race_info.get("skills", []):
                skill_name = skill_data.get("name")
                skill_bonus = skill_data.get("bonus")
                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={"bonus": skill_bonus, "race": race}
                )

            guild_info = player_data.get("guild")
            guild = None
            if guild_info:
                guild_name = guild_info.get("name")
                guild_description = guild_info.get("description")
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                )

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data.get("email"),
                    "bio": player_data.get("bio", ""),
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
