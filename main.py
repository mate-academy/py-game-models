import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_data = {}
    with open("players.json", "r") as file_obj:
        players_data = json.load(file_obj)  # data collected

    for player_key, player_data in players_data.items():
        race_data = player_data["race"]
        race_name = race_data["name"]
        race_description = race_data["description"]

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        for skill in race_data["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]

            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race_obj
            )

        guild_obj = None
        if player_data.get("guild") is not None:
            guild_data = player_data["guild"]
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        Player.objects.get_or_create(
            nickname=player_key,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
