import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for name, player in players.items():
            race_name = player["race"]["name"]
            race_description = player["race"]["description"]
            player_race, created = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description}
            )

            skills = player["race"]["skills"]
            for skill in skills:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                player_skill, created = Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={"bonus": skill_bonus, "race": player_race}
                )

            player_guild = None
            if player["guild"] is not None:
                guild_name = player["guild"]["name"]
                guild_description = player["guild"]["description"]
                player_guild, created = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                )

            Player.objects.create(
                nickname=name,
                email=player["email"],
                bio=player["bio"],
                race=player_race,
                guild=player_guild,
            )


if __name__ == "__main__":
    main()
