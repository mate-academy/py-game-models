import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_nickname, player_data in players.items():
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skills_data in race_data["skills"]:
            if not Skill.objects.filter(name=skills_data["name"]).exists():
                Skill.objects.create(
                    name=skills_data["name"],
                    bonus=skills_data["bonus"], race=race
                )

        guild_data = player_data["guild"]
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
