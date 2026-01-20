import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_info = player_data.get("race", {})
        race_name = race_info.get("name")
        race_description = race_info.get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description},
        )

        skills_data = race_info.get("skills", [])
        for skill_info in skills_data:
            skill_name = skill_info.get("name")
            skill_bonus = skill_info.get("bonus", "")

            Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_bonus},
            )

        guild_info = player_data.get("guild")
        guild = None
        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
