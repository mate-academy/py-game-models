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

        if not Race.objects.filter(name=race_name).exists():
            race_obj = Race.objects.create(
                name=race_name,
                description=race_description
            )
        else:
            race_obj = Race.objects.get(name=race_name)

        for skill in race_data["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_obj
                )

        guild_obj = None
        if guild_data := player_data["guild"]:
            guild_name = guild_data["name"]
            if not Guild.objects.filter(name=guild_name).exists():
                guild_description = guild_data["description"]
                guild_obj = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            else:
                guild_obj = Guild.objects.get(name=guild_name)

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
