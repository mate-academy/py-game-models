import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for nickname, player_data in players.items():
            player_race = player_data["race"]
            race_obj, _ = Race.objects.get_or_create(
                name=player_race["name"],
                defaults={"description": player_race["description"]}
            )

            for skill in player_race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    race=race_obj,
                    defaults={"bonus": skill.get("bonus")}
                )

            player_guild = player_data.get("guild")
            if player_guild:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=player_guild["name"],
                    defaults={"description": player_guild["description"]}
                )
            else:
                guild_obj = None

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race_obj,
                    "guild": guild_obj,
                }
            )


if __name__ == "__main__":
    main()
