import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        players_data = json.load(data)

    for nickname, player_data in players_data.items():

        race_data = player_data["race"]
        race = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )[0]

        if skills := race_data["skills"]:
            Skill.objects.bulk_create(
                [
                    Skill(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )
                    for skill in skills
                    if not Skill.objects.filter(name=skill["name"]).exists()
                ]
            )

        guild_data = player_data.get("guild")
        guild = (
            Guild.objects.get_or_create(**guild_data)[0]
            if guild_data else None
        )
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
