import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

with open("players.json", "r") as sourse:
    data = json.load(sourse)


def main() -> None:
    for nickname, info in data.items():
        if info["race"]:
            name_race = (
                info["race"]["name"] if
                info["race"]["name"] else None
            )
            race_description = (
                info["race"]["description"] if
                info["race"]["description"] else None
            )

            if not Race.objects.filter(name=name_race).exists():
                race = Race(
                    name=name_race,
                    description=race_description
                )
                race.save()
                race_id = Race.objects.get(name=name_race).id
        else:
            race_id = None

        if info["guild"]:
            guild_name = (
                info["guild"]["name"] if
                info["guild"]["name"] else None)
            guild_description = (
                info["guild"]["description"] if
                info["guild"]["description"] else None)

            if not Guild.objects.filter(name=guild_name).exists():
                guild_object = Guild(
                    name=guild_name,
                    description=guild_description
                )
                guild_object.save()

            guild_id = Guild.objects.get(name=guild_name).id
        else:
            guild_id = None

        if info["race"]["skills"]:
            for skill in info["race"]["skills"]:
                name_skill = skill["name"] if skill["name"] else None
                bonus = skill["bonus"] if skill["bonus"] else None
                if not Skill.objects.filter(name=name_skill).exists():
                    skill_object = Skill(
                        name=name_skill,
                        bonus=bonus,
                        race_id=race_id)
                    skill_object.save()

        email = info["email"] if info["email"] else None
        biography = info["bio"] if info["bio"] else None

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=biography,
            race_id=race_id,
            guild_id=guild_id
        )


if __name__ == "__main__":
    main()
