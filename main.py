import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for nickname, player in players.items():
        race_data = player["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data["skills"]:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race_obj,
                }
            )

        guild_data = player.get("guild")

        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )
        else:
            guild_obj = None

        player_obj, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
