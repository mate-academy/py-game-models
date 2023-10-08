import datetime
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


with open("players.json", "r") as file:
    data = json.load(file)


def main() -> None:
    data_model = data.items()
    for component in data_model:
        race_name = component[1].get("race").get("name")
        race_description = component[1].get("race").get("description")
        race, race_created = Race.objects.get_or_create(
            name=race_name,
            description=race_description,
        )
        for skills_name in component[1].get("race").get("skills"):
            name_skills = skills_name.get("name")
            bonus_skills = skills_name.get("bonus")
            Skill.objects.get_or_create(
                name=name_skills,
                bonus=bonus_skills,
                race=race,
            )

        if component[1].get("guild") is not None:
            name_guild = component[1].get("guild").get("name")
            description_guild = component[1].get("guild").get("description")
            guild, guild_create = Guild.objects.get_or_create(
                name=name_guild,
                description=description_guild,
            )

        guild = None if component[1].get("guild") is None else guild
        Player.objects.get_or_create(
            nickname=component[0],
            email=component[1].get("email"),
            bio=component[1].get("bio"),
            race=race,
            guild=guild,
            created_at=datetime.datetime.now(),
        )


if __name__ == "__main__":
    main()
