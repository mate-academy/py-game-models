import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with (open("players.json", "r") as file):
        players_data = json.load(file)
        print(players_data)

        for nickname, player_data in players_data.items():
            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=player_data["race"],
                default={"description": race_data.get("description", "")}
            )

            guild_data = player_data.het("guild", None)
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"],
                    default={"description": race_data.get("description", "")}
                )

            skills_data = race_data.get("skills")
            for skill_data in skills_data:
                Skill.objects.get_or_create(
                    name=skill_data["data"],
                    race=race,
                    defaults={"bonus": race_data.get("bonus", "")}
                )

            Player.objects.get_or_create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data.get("bonus", ""),
                race=race,
                guild=guild,

            )


if __name__ == "__main__":
    main()
