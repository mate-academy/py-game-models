import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for player, attributes in players.items():
        race, created = Race.objects.get_or_create(
            name=attributes["race"]["name"],
            description=attributes["race"]["description"]
        )

        for skill in attributes["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if attributes["guild"] is not None:
            guild_description = attributes["guild"]["description"] if attributes["guild"] else None
            guild, created = Guild.objects.get_or_create(
                name=attributes["guild"]["name"],
                description=guild_description
            )
        else:
            guild = None

        user = Player.objects.create(
            nickname=player,
            email=attributes["email"],
            bio=attributes["bio"],
            race=race,
            guild=guild
        )
        user.save()


if __name__ == "__main__":
    main()
