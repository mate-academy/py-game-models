import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_nickname, player in players.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]},
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill["bonus"]}
            )

        guild_data = player.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        Player.objects.update_or_create(
            nickname=player_nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
