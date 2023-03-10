import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as date:
        player_info = json.load(date)

    for player, info in player_info.items():
        race_name = info["race"]["name"]
        skills = info["race"]["skills"]

        race, created_race = Race.objects.get_or_create(
            name=race_name,
            description=info["race"]["description"]
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"],
                          "race": race
                          }
            )

        guild = None

        if info["guild"]:
            guild, created_guild = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                defaults={"description": info["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
