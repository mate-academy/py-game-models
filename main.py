import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_info in players.items():
        race_data = player_info.get("race", {})
        race, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )


        for skill in player_info.get("race", {}).get("skills"):
            skill_info, created = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
           )

        guild = player_info.get("guild", None)
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
        )

        player_name, created = Player.objects.get_or_create(
            nickname=player,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
