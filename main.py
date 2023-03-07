import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        player_info = json.load(data)

    for player, info in player_info.items():
        race_name = info["race"]["name"]
        skills = info["race"]["skills"]
        guild = info["guild"]["name"] if info["guild"] else None

        if not Race.objects.filter(name=race_name).exists():
            race_description = info["race"]["description"]
            Race.objects.create(name=race_name, description=race_description)

        race = Race.objects.get(name=race_name)

        for skill in skills:
            skill_name = skill["name"]
            if not Skill.objects.filter(name=skill_name).exists():
                skill_bonus = skill["bonus"]
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race_id=race.id
                )

        if guild:
            if not Guild.objects.filter(name=guild).exists():
                guild_description = info["guild"]["description"]
                Guild.objects.create(name=guild, description=guild_description)

            guild = Guild.objects.get(name=guild)

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
