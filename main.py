import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        guild_data = player_info["guild"]
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )

        skills_data = player_info["race"]["skills"]
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
