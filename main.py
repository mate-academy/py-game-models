import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname_data, item in players_data.items():
        race, created = Race.objects.get_or_create(
            name=item["race"]["name"],
            description=item["race"]["description"]
        )
        for skill_name in item["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_name["name"],
                bonus=skill_name["bonus"],
                race=race
            )
        guild_data = item.get("guild")
        if guild_data is not None:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname_data,
            email=item["email"],
            bio=item["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
