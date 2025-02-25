import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name", "Unknown Race")
        race_desc = race_data.get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc}
        )

        guild = None
        if player_data.get("guild"):
            guild_data = player_data["guild"]
            guild_name = guild_data.get("name", "Unknown Guild")
            guild_desc = guild_data.get("description", "")

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_desc}
            )

        skills = race_data.get("skills", [])
        for skill_data in skills:
            Skill.objects.get_or_create(
                name=skill_data.get("name", "Unknown Skill"),
                defaults={"bonus": skill_data.get("bonus", ""),
                          "race": race}
            )

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
