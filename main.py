import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
        for player, attributes in players.items():
            name = player  # name
            email = attributes["email"]  # email
            bio = attributes["bio"]
            attributes_race = attributes["race"]
            race_name = attributes_race["name"]  # race_name
            race_descript = attributes_race["description"]  # race_descript
            data_race, _ = Race.objects.get_or_create(
                name=race_name,
                description=race_descript
            )

            if attributes["guild"]:
                guild_name = attributes["guild"]["name"]
                guild_description = attributes["guild"]["description"]
                data_guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )

            for skill in attributes_race["skills"]:
                name_skill = skill["name"]  # name_skill
                bonus_skill = skill["bonus"]  # bonus_skill
                skill_obj, _ = Skill.objects.get_or_create(
                    name=name_skill,
                    bonus=bonus_skill,
                    race_id=data_race.id
                )

            Player.objects.get_or_create(nickname=name,
                                         email=email,
                                         bio=bio,
                                         race_id=data_race.id,
                                         guild_id=data_guild.id
                                         if attributes["guild"]
                                         else None)


if __name__ == "__main__":
    main()
