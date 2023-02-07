import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, info in data.items():
        guild_name = info["guild"]["name"] if info["guild"] else False
        if guild_name:
            guild_check = Guild.objects.filter(name=guild_name).exists()
            if not guild_check:
                guild_script = (
                    info["guild"]["description"]
                    if info["guild"]["description"] else None
                )
                guild = Guild.objects.create(
                    name=guild_name, description=guild_script
                )
            else:
                guild = Guild.objects.get(name=guild_name)

        race_name = info["race"]["name"]
        race_check = Race.objects.filter(name=race_name).exists()
        if race_check is False:
            race_script = (
                info["race"]["description"]
                if info["race"]["description"] else None
            )
            race = Race.objects.create(name=race_name, description=race_script)
            skill_package = (
                info["race"]["skills"] if info["race"]["skills"] else None
            )
            if skill_package:
                for item in skill_package:
                    skill_name, bonus = item["name"], item["bonus"]
                    Skill.objects.create(
                        name=skill_name, bonus=bonus, race_id=race.id
                    )
        else:
            race = Race.objects.get(name=race_name)

        email_ = info["email"]
        bio = info["bio"]
        Player.objects.create(
            nickname=nickname,
            email=email_,
            bio=bio,
            race_id=race.id,
            guild_id=guild.id if guild_name else None
        )


if __name__ == "__main__":
    main()
