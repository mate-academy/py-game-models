import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    for model in (Race, Skill, Player, Guild):
        model.objects.all().delete()

    with open("players.json", "r") as f:
        data = json.load(f)

    players = data
    for player_key, player_value in players.items():
        race, created = Race.objects.get_or_create(
            name=player_value["race"]["name"],
            description=player_value["race"]["description"]
        )

        for skill in range(len(player_value["race"]["skills"])):
            Skill.objects.get_or_create(
                name=player_value["race"]["skills"][skill]["name"],
                bonus=player_value["race"]["skills"][skill]["bonus"],
                race=race
            )

        guild = None
        if player_value.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_value["guild"]["name"],
                description=player_value["guild"]["description"]
            )

        Player.objects.create(
            nickname=player_key,
            email=player_value["email"],
            bio=player_value["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
