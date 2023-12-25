import init_django_orm  # noqa

import json
from db.models import Race, Skill, Guild, Player


def create_race_with_skills(data: dict) -> Race:
    race_name = data["name"]
    race, _ = Race.objects.get_or_create(
        name=race_name, defaults={"description": data.get("description", "")}
    )

    skills_data = data.get("skills", [])
    for skill_data in skills_data:
        skill, _ = Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={"bonus": skill_data["bonus"], "race": race}
        )

    return race


def create_guild(data: dict) -> Guild:
    if data is None:
        return None
    guild_name = data["name"]
    guild, _ = Guild.objects.get_or_create(
        name=guild_name, defaults={"description": data.get("description", "")}
    )
    return guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player_name, player_data in players_data.items():
        race = create_race_with_skills(player_data["race"])
        guild = create_guild(player_data["guild"])

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
