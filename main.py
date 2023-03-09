import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as date:
        player_info = json.load(date)
    for player, info in player_info.items():
        race_name = info["race"]["name"]
        skills = info["race"]["skills"]
        guild = info["guild"] if info["guild"] else None

        if not Race.objects.filter(name=race_name).exists():
            race_description = info["race"]["description"]
            race, created_race = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race.id
                )

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            guild = Guild.objects.get(name=guild["name"])

        if not Player.objects.filter(nickname=player).exists():
            email = info["email"]
            bio = info["bio"]
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race_id=race.id,
                guild=guild
            )


if __name__ == "__main__":
    main()
