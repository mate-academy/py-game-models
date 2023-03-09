import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        player_list = json.load(file)
    print(player_list)

    for player_name, player_data in player_list.items():
        guild = None
        if player_data["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"],
            )

        race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )
        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )


if __name__ == "__main__":
    main()
