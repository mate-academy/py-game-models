import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

        for player_name, player_data in data.items():
            race_data = player_data.get("race")

            if race_data:
                race_name = race_data["name"]
                race_description = race_data.get("description", "")
                race, _ = Race.objects.get_or_create(name=race_name, description=race_description)
                skills_data = race_data.get("skills", [])
                for skill_data in skills_data:
                    skill_name = skill_data["name"]
                    skill_bonus = skill_data["bonus"]
                    Skill.objects.get_or_create(name=skill_name, bonus=skill_bonus, race=race)
            else:
                race = None

            guild_data = player_data.get("guild")
            if guild_data:
                guild_name = guild_data["name"]
                guild_description = guild_data.get("description", "")
                guild, _ = Guild.objects.get_or_create(name=guild_name, description=guild_description)
            else:
                guild = None

            Player.objects.create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
