import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

        for nickname, player_data in data.items():
            race_data = player_data.get("race", {})
            race, is_created = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description"),
            )
            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data.get("name"),
                    bonus=skill_data.get("bonus"),
                    race=race,
                )

            guild_data = player_data.get("guild")
            guild = None
            if guild_data:
                guild, is_created = Guild.objects.get_or_create(
                    name=guild_data.get("name"),
                    description=guild_data.get("description"),
                )

            Player.objects.create(
                nickname=nickname,
                email=player_data.get("email"),
                bio=player_data.get("bio"),
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
