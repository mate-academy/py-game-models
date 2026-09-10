import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_dict = {}
    with open("players.json") as file_data:
        players_dict = json.load(file_data)

    for key, value in players_dict.items():
        guild = value.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                defaults=dict(description=guild.get("description"))
            )
        race, _ = Race.objects.get_or_create(
            name=value.get("race").get("name"),
            defaults=dict(description=value.get("race").get("description"))
        )
        for skill in value.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults=dict(bonus=skill.get("bonus"), race=race)
            )
        Player.objects.get_or_create(
            nickname=key,
            defaults=dict(
                email=value.get("email"),
                bio=value.get("bio"),
                race=race,
                guild=guild
            )
        )


if __name__ == "__main__":
    main()
