
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():

        nickname = player_name
        email = player_data["email"]
        bio = player_data["bio"]

        race_data = player_data["race"]
        race_name = race_data["name"]
        race_description = race_data["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        guild_data = player_data["guild"]
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )

        skills_data = race_data["skills"]
        for skill_data in skills_data:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )


if __name__ == "__main__":
    main()
