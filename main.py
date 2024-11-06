import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
        for nickname, player_dict in players.items():
            guild = None
            if player_dict.get("guild"):
                guild_name = player_dict["guild"]["name"]
                guild_description = player_dict["guild"].get("description")
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                )

            race_name = player_dict["race"]["name"]
            race_description = player_dict["race"].get("description")
            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description}
            )

            Player.objects.create(
                nickname=nickname,
                email=player_dict["email"],
                bio=player_dict["bio"],
                race=race,
                guild=guild
            )

            for skill_data in player_dict["race"].get("skills", []):
                skill_name = skill_data["name"]
                bonus = skill_data["bonus"]
                skill, _ = Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=bonus,
                    race=race
                )


if __name__ == "__main__":
    main()
