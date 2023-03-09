import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for name, player_info in players.items():
        race = player_info["race"]["name"]
        race_descript = player_info["race"]["description"]
        race_skills = player_info["race"]["skills"]

        if Race.objects.filter(name=race).exists():
            Race.objects.get(name=race)
        else:
            Race.objects.create(name=race,
                                description=race_descript)

        if race_skills:
            for skill in race_skills:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                skill_race = Race.objects.get(name=race)

                if Skill.objects.filter(name=skill_name).exists():
                    Skill.objects.get(name=skill_name)
                else:
                    Skill.objects.create(name=skill_name,
                                         bonus=skill_bonus,
                                         race=skill_race)

        if player_info["guild"]:
            guild_name = player_info["guild"]["name"]
            guild_description = player_info["guild"]["description"]

            if Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.get(name=guild_name)
            else:
                guild = Guild.objects.create(name=guild_name,
                                             description=guild_description)
        else:
            guild = None

        race = Race.objects.get(name=player_info["race"]["name"])

        Player.objects.create(nickname=name,
                              email=player_info["email"],
                              bio=player_info["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
