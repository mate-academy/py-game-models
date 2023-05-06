import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_json:
        dict_with_players = json.load(players_json)

    for player_name, player_info in dict_with_players.items():
        player_race_info = player_info["race"]
        player_skills_info = player_race_info["skills"]
        player_guild_info = player_info["guild"]

        race_instance, _ = Race.objects.get_or_create(
            name=player_race_info["name"],
            description=player_race_info["description"]
        )

        for skill in player_skills_info:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_instance
            )

        if player_guild_info:
            guild_instance, _ = Guild.objects.get_or_create(
                name=player_guild_info["name"],
                description=player_guild_info["description"]
            )
        else:
            guild_instance = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
