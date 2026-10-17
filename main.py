import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        data = json.load(data_file)

    for player_name, player_data in data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )

        for skill_data in player_data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description"),
            )

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            guild_id=guild.id if guild else None,
            race_id=race.id,
        )


if __name__ == "__main__":
    main()
