import init_django_orm  # noqa: F401


import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name", "")
        race_description = race_data.get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name", "")
            skill_bonus = skill_data.get("bonus", "")

            Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_bonus}
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name", "")
            guild_description = guild_data.get("description", None)

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
