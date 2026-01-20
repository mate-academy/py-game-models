import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_str, player_json in data.items():
        guild_json = player_json.get("guild")
        if guild_json:
            description = guild_json.get("description")
            if not description:
                guild_obj, _ = (
                    Guild.objects.get_or_create(name=guild_json.get("name")))
            else:
                guild_obj, _ = (
                    Guild.objects.get_or_create(name=guild_json.get("name"),
                                                description=description))

        race_js = player_json.get("race")
        if race_js:
            description = race_js.get("description")
            if not description:
                description = ""
            race_obj, _ = Race.objects.get_or_create(name=race_js.get("name"),
                                                     description=description)
            skills_json = player_json.get("race").get("skills")
            fill_skills(skills_json, race_obj)

        nickname = player_str
        email = player_json.get("email")
        bio = player_json.get("bio")
        if guild_json:
            Player.objects.get_or_create(nickname=nickname,
                                         email=email, bio=bio,
                                         race=race_obj,
                                         guild=guild_obj)
        else:
            Player.objects.get_or_create(nickname=nickname,
                                         email=email,
                                         bio=bio,
                                         race=race_obj)


def fill_skills(skills_json: list[dict], race_obj: Race) -> None:
    for skill in skills_json:
        bonus_prepared = skill.get("bonus")
        skill_obj, _ = Skill.objects.get_or_create(name=skill.get("name"),
                                                   bonus=bonus_prepared,
                                                   race=race_obj)


if __name__ == "__main__":
    main()
