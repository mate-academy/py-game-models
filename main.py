import datetime
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for name_data, info in data.items():
        race_name = info.get("race").get("name")
        race_description = info.get("race").get("description")
        race, race_created = Race.objects.get_or_create(
            name=race_name,
            description=race_description,
        )
        for skills_name in info.get("race").get("skills"):
            name_skills = skills_name.get("name")
            bonus_skills = skills_name.get("bonus")
            Skill.objects.get_or_create(
                name=name_skills,
                bonus=bonus_skills,
                race=race,
            )

        if info.get("guild") is not None:
            name_guild = info.get("guild").get("name")
            description_guild = info.get("guild").get("description")
            guild, guild_create = Guild.objects.get_or_create(
                name=name_guild,
                description=description_guild,
            )

        guild = None if info.get("guild") is None else guild
        Player.objects.get_or_create(
            nickname=name_data,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild,
            created_at=datetime.datetime.now(),
        )


if __name__ == "__main__":
    main()
