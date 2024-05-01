import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players_data = json.load(data_file)

    for player_name, player_data in players_data.items():
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
        guild = None
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        skill_data = race_data["skills"]
        for skill_item in skill_data:
            skill_name = skill_item["name"]
            skill_bonus = skill_item["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                race_id=race.id,
                bonus=skill_bonus
            )

        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race_id=race.id,
            guild=guild
        )


if __name__ == "__main__":
    main()
