import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as players_file:
        players = json.load(players_file)

    for player_name, data in players.items():

        race_data = data.get("race", {})
        race_name = race_data.get("name", "")
        race_description = race_data.get("description", "")
        race_skills = race_data.get("skills", [])

        player_race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in race_skills:
            skill_name = skill_data.get("name", "")
            skill_bonus = skill_data.get("bonus", 0)

            Skill.objects.get_or_create(
                name=skill_name,
                race=player_race,
                defaults={"bonus": skill_bonus}
            )

        guild_data = data.get("guild")
        player_guild = None

        if isinstance(guild_data, dict):
            guild_name = guild_data.get("name", "")
            guild_description = guild_data.get("description", "")

            player_guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": data.get("email", ""),
                "bio": data.get("bio", ""),
                "race": player_race,
                "guild": player_guild,
            },
        )


if __name__ == "__main__":
    main()
