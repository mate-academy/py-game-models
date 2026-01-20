import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:

    with open("players.json", "rb") as json_file:
        objects = json.load(json_file)
        for key in objects:
            skills_list = objects[key]["race"].pop("skills")
            guild_dict = objects[key].pop("guild")
            guild = None
            if guild_dict:
                guild = Guild.objects.get_or_create(**guild_dict)[0]

            race = Race.objects.get_or_create(**objects[key].pop("race"))[0]

            for skill in skills_list:
                Skill.objects.get_or_create(
                    **skill,
                    race=race
                )

            Player.objects.get_or_create(
                nickname=key,
                **objects[key],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
