import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for nickname, player_data in players.items():
        nickname = nickname
        email = player_data["email"]
        bio = player_data["bio"]
        race_name = player_data["race"]["name"]
        race_description = player_data["race"]["description"]
        if player_data["guild"]:
            guild_name = player_data["guild"]["name"]
            guild_description = player_data["guild"]["description"]
        skills = player_data["race"]["skills"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(name=race_name,
                                description=race_description
                                )
        race = Race.objects.get(name=race_name)
        guild = None
        if player_data["guild"]:
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            guild = Guild.objects.get(name=guild_name)
        for skill in skills:
            skill_name = skill["name"]
            bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=bonus,
                    race=race
                )
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
