import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)
    for player_name, player_detail in players_info.items():
        email = player_detail["email"]
        bio = player_detail["bio"]
        race_info = player_detail["race"]
        guild_info = player_detail.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        for skill_info in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info["bonus"],
                race=race
            )

        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
