import init_django_orm  # noqa: F401
import json
from django.utils import timezone
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    if isinstance(data, dict):
        players = data.get("players", data)
        if isinstance(players, dict):
            players_list = players.values()
        else:
            players_list = players
    else:
        players_list = data

    for player_data in players_list:
        nickname = player_data.get("nickname")
        email = player_data.get("email")

        if not nickname or not email:
            continue

        race_data = player_data.get("race")
        if not race_data:
            continue

        if isinstance(race_data, dict):
            race_name = race_data.get("name")
            race_desc = race_data.get("description", "")
            skills_list = race_data.get("skills", [])
        else:
            race_name = race_data
            race_desc = ""
            skills_list = []

        if not race_name:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc},
        )

        guild = None
        guild_data = player_data.get("guild")
        if guild_data:
            if isinstance(guild_data, dict):
                guild_name = guild_data.get("name")
                guild_desc = guild_data.get("description")
            else:
                guild_name = guild_data
                guild_desc = None

            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_desc},
                )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
                "created_at": timezone.now(),
            },
        )

        for skill_data in skills_list:
            skill_name = skill_data.get("name")
            skill_bonus = skill_data.get("bonus")
            if skill_name and skill_bonus:
                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "bonus": skill_bonus,
                        "race": race,
                    },
                )


if __name__ == "__main__":
    main()
