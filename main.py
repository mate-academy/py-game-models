import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for name, player_info in players.items():
        race_name = player_info["race"]["name"]
        race_descript = player_info["race"]["description"]
        race_skills = player_info["race"]["skills"]

        race, created = Race.objects.get_or_create(
            name=race_name,
            description=race_descript
        )

        if race_skills:
            for skill in race_skills:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")

                if not Skill.objects.filter(name=skill_name).exists():
                    Skill.objects.create(name=skill_name,
                                         bonus=skill_bonus,
                                         race=race)

        guild = None
        if player_info["guild"]:
            guild_name = player_info["guild"]["name"]
            guild_description = player_info["guild"]["description"]

            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        Player.objects.create(nickname=name,
                              email=player_info["email"],
                              bio=player_info["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
