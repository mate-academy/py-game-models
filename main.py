import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main(player=None) -> None:
    pass
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data.get("guild")
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description")}
        )
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
            )
            player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
