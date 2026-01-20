import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for player_name, player_data in players_data.items():
        guild_ = None
        if player_data["guild"]:
            guild_, _ = (
                Guild.objects.
                get_or_create(**player_data["guild"])
            )
        race_, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"],
        )
        if player_data["race"]["skills"]:
            for skill in player_data["race"]["skills"]:
                skill_, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=Race.objects.get(name=race_.name).id
                )

        player_, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race_id=Race.objects.get(name=race_.name).id,
        )
        player_.guild = guild_
        player_.save()


if __name__ == "__main__":
    main()
