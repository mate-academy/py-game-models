import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

        for nickname, player_info in players.items():

            race_info = player_info["race"]
            race, _ = Race.objects.get_or_create(
                name=race_info["name"],
                defaults={"description": race_info.get("description")},
            )

            for skill in race_info["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild_info = player_info["guild"]
            guild = None
            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description")},
                )

            Player.objects.create(
                nickname=nickname,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
