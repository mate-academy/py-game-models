import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        email = player_data["email"]
        bio = player_data["bio"]
        race_data = player_data["race"]
        skills_data = race_data["skills"]
        guild_data = player_data["guild"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

    if guild_data:
        guild, _ = Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"]
        )
    else:
        guild = None

    skills = []
    for skill_data in skills_data:
        skill, _ = Skill.objects.get_or_create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race
        )
        skills.append(skill)

    Player.objects.bulk_create(
        nickname=player_name,
        email=email,
        bio=bio,
        race=race,
        guild=guild
    )


if __name__ == "__main__":
    main()
