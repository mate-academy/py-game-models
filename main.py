import json

import init_django_orm  # noqa: F401
from db.models import Race, Guild, Skill, Player


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)
        for player_name, add_data in players.items():

            # Race
            race_name = add_data.get("race", {}).get("name")
            race_description = add_data.get("race", {}).get("description")
            if not Race.objects.filter(name=race_name).exists():
                race_player = Race.objects.create(name=race_name,
                                                  description=race_description)

            # Guild
            if add_data.get("guild"):
                guild_name = add_data.get("guild", {}).get("name")
                guild_descr = add_data.get("guild", {}).get("description")
                if not Guild.objects.filter(name=guild_name).exists():
                    guild_player = Guild.objects.create(
                        name=guild_name,
                        description=guild_descr)
            else:
                guild_player = None

            # Skill
            list_of_skills = add_data.get("race", {}).get("skills")
            if list_of_skills:
                for skill in list_of_skills:
                    skill_name = skill.get("name")
                    race_skill = Race.objects.get(name=race_name)
                    if not Skill.objects.filter(name=skill_name).exists():
                        Skill.objects.create(name=skill_name,
                                             bonus=skill.get("bonus"),
                                             race=race_skill)

            # Player
            if not Player.objects.filter(nickname=player_name).exists():
                Player.objects.create(nickname=player_name,
                                      email=add_data.get("email"),
                                      bio=add_data.get("bio"),
                                      race=race_player,
                                      guild=guild_player
                                      )


if __name__ == "__main__":
    main()
