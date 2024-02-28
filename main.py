import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_data = json.load(file)

    for player, value in player_data.items():
        guild = None
        if guild_value := value.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=guild_value["name"],
                description=guild_value["description"]
            )

        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        Player.objects.create(
            nickname=player,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    Player.objects.all().delete()
    Guild.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    main()
