import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players_data = json.load(players)
        for player, data in players_data.items():
            nickname = player
            email = data["email"]
            bio = data["bio"]
            race_name = data["race"]["name"]
            race_description = data["race"]["description"]

            race_info = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )
            print(race_info)
            guild_data = data["guild"]
            if guild_data is not None:
                guild_name = guild_data["name"]
                guild_description = guild_data["description"]
                guild_info = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )
            else:
                guild_info = None

            skill_data = data["race"]["skills"]
            for skill in skill_data:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_info[0]
                )
            Player.objects.get_or_create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race_info[0],
                guild=guild_info[0] if guild_info is not None else None
            )


if __name__ == "__main__":
    main()
