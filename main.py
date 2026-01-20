import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as read_data:
        data = json.load(read_data)

    for person_name, info in data.items():

        email, bio, race, guild = info.values()

        race_name, race_descr, race_skills = race.values()
        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_descr
        )
        guild_obj = None
        if guild:
            guild_name, guild_descr = guild.values()
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_descr
            )
        if race_skills:
            for skill in race_skills:
                skill_name, bonus = skill.values()
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=bonus,
                    race=race_obj
                )
        Player.objects.create(
            nickname=person_name,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
