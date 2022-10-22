import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_info = json.load(file)

    for player, data in players_info.items():
        race_info = data["race"]
        if race_info:
            if not Race.objects.filter(name=race_info["name"]).exists():
                race = Race.objects.create(
                    name=race_info["name"],
                    description=race_info["description"]
                )
            else:
                race = Race.objects.get(name=race_info["name"])

        skill_info = race_info["skills"]
        if skill_info:
            for skill in skill_info:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        guild_info = data["guild"]
        guild = None
        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_info["name"])

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                guild=guild,
                race=race,

            )


if __name__ == "__main__":
    main()
