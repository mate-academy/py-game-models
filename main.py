import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_file:
        data = json.load(data_file)
    for player, player_data in data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = None

        if player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
