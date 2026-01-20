import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        player_email = player_data["email"]
        player_bio = player_data["bio"]

        race_data = player_data["race"]

        race_name = race_data["name"]
        race_description = race_data["description"]
        race = Race.objects.get_or_create(
            name=race_name,
            description=race_description,
        )[0]

        for skill in race_data["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race,
            )

        if guild_data := player_data["guild"]:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            guild_obj = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )[0]
        else:
            guild_obj = None

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=race,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
