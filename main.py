import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        data = json.load(players_file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]
        skills = race_data.pop("skills")

        race, _ = Race.objects.get_or_create(**race_data)

        for skill_data in skills:
            Skill.objects.get_or_create(
                **skill_data,
                race=race,
            )

        guild_data = player_data["guild"]
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(**guild_data)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
