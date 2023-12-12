import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        player_data = json.load(player_file)

    for player, data in player_data.items():
        race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )[0]

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild_data = data["guild"] or None
        if guild_data:
            guild_data = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )[0]

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild_data
        )


if __name__ == "__main__":
    main()
