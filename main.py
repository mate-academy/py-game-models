import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as f:
        players = json.load(f)

    for nickname, player_info in players.items():
        race_info = player_info["race"]
        if not Race.objects.filter(name=race_info["name"]).exists():
            race = Race.objects.create(
                name=race_info["name"],
                description=race_info["description"]
            )
        else:
            race = Race.objects.get(name=race_info["name"])

        skills = race_info["skills"]
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild_info = player_info["guild"]
        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_info["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
