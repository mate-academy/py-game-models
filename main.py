import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    with open("players.json", "r") as file:
        player_data = json.load(file)

    for player_name, player_info in player_data.items():
        player_race, _ = Race.objects.get_or_create(
            name=player_info["race"].get("name"),
            defaults={"description": player_info["race"].get("description")}
        )

        player_guild = player_info.get("guild")
        if player_guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"].get("name"),
                defaults={"description": player_info["guild"].get(
                    "description")}
            )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"bonus": skill.get("bonus"), "race": player_race}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
