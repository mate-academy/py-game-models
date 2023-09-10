import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        nickname = player_name
        email = player_info["email"]
        bio = player_info["bio"]
        race = player_info["race"]

        race_name = race["name"]
        race_description = race["description"]

        if Race.objects.filter(name=race_name).exists():
            race_value = Race.objects.filter(name=race_name)[0]
        else:
            race_value = Race.objects.create(
                name=race_name, description=race_description
            )

        skills = race["skills"]
        for skill in skills:
            name = skill["name"]
            bonus = skill["bonus"]
            if not Skill.objects.filter(name=name).exists():
                Skill.objects.create(name=name, bonus=bonus, race=race_value)

        guild = player_info.get("guild")
        guild_value = None
        if guild is not None:
            guild_name = guild["name"]
            guild_description = guild["description"]
            if Guild.objects.filter(name=guild_name).exists():
                guild_value = Guild.objects.filter(name=guild_name)[0]
            else:
                guild_value = Guild.objects.create(
                    name=guild_name, description=guild_description
                )
        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race_value,
                guild=(guild_value if guild else None),
            )


if __name__ == "__main__":
    main()
