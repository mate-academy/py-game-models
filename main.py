import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for nickname, player_data in players_data.items():
        guild = None
        if guild_data := player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"],
        )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
