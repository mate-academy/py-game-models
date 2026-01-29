import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as f:
        data = json.load(f)

    for name, info in data.items():
        guild = None
        nickname = name
        email = info.get("email")
        bio = info.get("bio")
        race_data = info.get("race")
        guild_inf = info.get("guild")

        if race_data and isinstance(race_data, dict):
            name_race = race_data.get("name")
            description_race = race_data.get("description")
            race, created = Race.objects.get_or_create(
                name=name_race,
                description=description_race
            )

            skills_race = race_data.get("skills")
            if skills_race and isinstance(skills_race, list):
                for skill in skills_race:
                    Skill.objects.get_or_create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race
                    )

            if guild_inf and isinstance(guild_inf, dict):
                guild_name = guild_inf.get("name")
                guild_description = guild_inf.get("description")

                guild, created = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )

            Player.objects.get_or_create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
