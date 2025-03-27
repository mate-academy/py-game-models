import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    if not players_data:
        print("The JSON file is empty or has an invalid structure.")
        return

    for nickname, player in players_data.items():
        race_data = player.get("race", {})
        race_name = race_data.get("name")
        race_desc = race_data.get("description", "")
        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc}
        )

        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = None
        guild_data = player.get("guild", {})
        if guild_data:
            guild_name = guild_data.get("name")
            guild_desc = guild_data.get("description", "")
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_desc}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild if guild_name else None,
        )


if __name__ == "__main__":
    main()
