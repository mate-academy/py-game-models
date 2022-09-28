import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_key, player_val in data.items():
        player_name = player_key
        player_email = player_val["email"]
        player_bio = player_val["bio"]
        race_name = player_val["race"]["name"]
        race_description = player_val["race"]["description"]

        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(name=race_name, description=race_description)
        race_id = Race.objects.get(name=race_name)

        guild_id = None
        if player_val["guild"] is not None:
            guild_name = player_val["guild"]["name"]

            if not Guild.objects.filter(name=guild_name).exists():
                if player_val["guild"]["description"] is not None:
                    guild_description = player_val["guild"]["description"]
                    Guild.objects.create(name=guild_name, description=guild_description)
                else:
                    Guild.objects.create(name=guild_name)
                guild_id = Guild.objects.get(name=guild_name).id
            else:
                guild_id = Guild.objects.get(name=guild_name).id

        skills = player_val["race"]["skills"]
        for skill in skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(name=skill_name, bonus=skill_bonus, race_id=race_id.id)

        if not Player.objects.filter(nickname=player_name):
            Player.objects.create(nickname=player_name,
                                  email=player_email,
                                  bio=player_bio,
                                  race_id=race_id.id,
                                  guild_id=guild_id
                                  )


if __name__ == "__main__":
    main()
