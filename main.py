import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name", "").strip()
        race_description = race_data.get("description", "")
        skills = race_data.get("skills", [])

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in skills:
            skill_name = skill_data.get("name", "").strip()
            skill_bonus = skill_data.get("bonus", "")
            if skill_name:
                Skill.objects.get_or_create(
                    name=skill_name,
                    race=race,
                    defaults={"bonus": skill_bonus}
                )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name", "").strip()
            guild_description = guild_data.get("description", "")
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
            if not created and guild.description != guild_description:
                guild.description = guild_description
                guild.save()

        Player.objects.update_or_create(
            nickname=nickname.strip(),
            defaults={
                "email": player_data.get("email", "").strip(),
                "bio": player_data.get("bio", "").strip(),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
