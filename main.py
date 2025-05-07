import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_info in players_data.items():
        race_data = player_info.get("race")
        guild_data = player_info.get("guild")
        guild_name = guild_data.get("name") if guild_data else None
        skills_data = race_data.get("skills", []) if race_data else []

        race, created_race = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        ) if race_data else (None, False)

        guild, created_guild = Guild.objects.get_or_create(
            name=guild_name,
            defaults={"description": guild_data.get("description")}
            if guild_data else {}
        ) if guild_name else (None, False)

        player = Player(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )
        player.save()

        if race:
            for skill_info in skills_data:
                skill, created_skill = Skill.objects.get_or_create(
                    name=skill_info["name"],
                    race=race,
                    defaults={"bonus": skill_info.get("bonus", "")}
                )

        print(f"Added player: {nickname}")


if __name__ == "__main__":
    main()
