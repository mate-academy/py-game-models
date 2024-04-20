import json

import init_django_orm  # noqa: F401

from django.utils.timezone import now

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_name = player_data["race"]["name"]
        race, _ = Race.objects.get_or_create(name=race_name)

        guild_data = player_data.get("guild", None)
        if guild_data:
            guild_name = guild_data["name"]
            guild, _ = Guild.objects.get_or_create(name=guild_name)
        else:
            guild = None

        skills_data = player_data["race"]["skills"]
        for skill_data in skills_data:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
            created_at=now()
        )


if __name__ == "__main__":
    main()
