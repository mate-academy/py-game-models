import init_django_orm  # noqa: F401
from db.models import Player, Guild, Race, Skill
import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        guild_data = player_info.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_data.get("description", "")}
                )

        race_data = player_info.get("race")
        race = None
        if race_data:
            race_name = race_data.get("name")
            if race_name:
                race, _ = Race.objects.get_or_create(
                    name=race_name,
                    defaults={"description": race_data.get("description", "")}
                )

                for skill in race_data.get("skills", []):
                    skill_name = skill.get("name")
                    skill_bonus = skill.get("bonus", 0)
                    if skill_name is not None:
                        Skill.objects.get_or_create(
                            name=skill_name,
                            bonus=skill_bonus,
                            race=race
                        )

        Player.objects.create(
            nickname=nickname,
            email=player_info.get("email", ""),
            bio=player_info.get("bio", ""),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
