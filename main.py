import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for player_name, player_data in players.items():
            email = player_data.get("email")
            bio = player_data.get("bio")
            race_data = player_data.get("race")
            skills_data = race_data.get("skills")
            guild_data = player_data.get("guild")

            current_race, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description")
            )

            if guild_data:
                current_guild, _ = Guild.objects.get_or_create(
                    name=guild_data.get("name"),
                    description=guild_data.get("description")
                )
            else:
                current_guild = None

            skills = []
            for skill_data in skills_data:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    bonus=skill_data.get("bonus"),
                    race=current_race
                )
                skills.append(skill)

            Player.objects.get_or_create(
                nickname=player_name,
                email=email,
                bio=bio,
                race=current_race,
                guild=current_guild
            )


if __name__ == "__main__":
    main()
