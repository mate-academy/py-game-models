import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for nickname, info in data.items():
        race_info = info.get("race")
        race, is_race_created = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={
                "description": race_info.get("description", "")
            }
        )
        skills_info = race_info.get("skills")
        for skill_info in skills_info:
            skill, is_skill_created = Skill.objects.get_or_create(
                name=skill_info.get("name"),
                defaults={
                    "bonus": skill_info.get("bonus"),
                    "race": race
                }
            )

        guild_info = info.get("guild")
        guild = None
        if guild_info:
            guild, is_guild_created = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={
                    "description": guild_info.get("description")
                }
            )

        player, is_player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race,
                "guild": guild,
            }
        )

if __name__ == "__main__":
    main()
