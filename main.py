import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        guild_name = (
            player_data["guild"]["name"]
            if player_data["guild"]
            else None
        )

        if player_data["guild"]:
            guild_description = player_data["guild"].get("description")
        else:
            guild_description = None
            guild = None
        if guild_name and not Guild.objects.filter(
                name=guild_name
        ).exists():
            guild = Guild.objects.create(
                name=guild_name,
                description=guild_description
            )

        race_name = (
            player_data["race"]["name"]
            if player_data["race"]
            else None
        )
        race_description = player_data["race"].get("description")

        if race_name and not Race.objects.filter(
                name=race_name
        ).exists():
            race = Race.objects.create(
                name=race_name,
                description=race_description
            )

        for skill_data in player_data["race"]["skills"]:
            skill_name = skill_data["name"] if skill_data else None
            skill_bonus = skill_data.get("bonus")
            if skill_name and not Skill.objects.filter(
                    name=skill_name
            ).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )

        player_nickname = player_name
        player_email = player_data["email"]
        player_bio = player_data["bio"]
        if not Player.objects.filter(
                nickname=player_nickname
        ).exists():
            Player.objects.create(
                nickname=player_nickname,
                email=player_email,
                bio=player_bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
