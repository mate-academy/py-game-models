import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for player_nickname, player_data in players.items():
        current_race, _ = Race.objects.get_or_create(name=player_data[
            "race"
        ]["name"], defaults={"description": player_data[
            "race"
        ].get("description", "")})

        for skill in player_data.get("skills", []):
            Skill.objects.get_or_create(name=skill[
                "name"
            ], defaults={"bonus": skill.get("bonus",
                                            ""), "race": current_race})

        if player_data.get("guild") is None:
            current_guild = None
        else:
            current_guild, _ = Guild.objects.get_or_create(name=player_data[
                "guild"
            ]["name"], defaults={"description": player_data[
                "guild"
            ].get("description")})
        Player.objects.get_or_create(nickname=player_nickname,
                                     defaults={
                                         "email": player_data.get("email"),
                                         "bio": player_data.get("bio"),
                                         "race": current_race,
                                         "guild": current_guild
                                     })


if __name__ == "__main__":
    main()
