import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, player_fields in players.items():
        email = player_fields["email"]
        bio = player_fields["bio"]
        race = create_race_and_skills(player_fields["race"])
        guild = create_guild(player_fields["guild"]) \
            if player_fields["guild"] else None

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


def create_guild(guild_fields: dict) -> Guild:
    guild, _ = Guild.objects.get_or_create(
        name=guild_fields["name"],
        defaults={"description": guild_fields["description"]}
    )
    return guild


def create_race_and_skills(race_fields: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_fields["name"],
        defaults={"description": race_fields["description"]}
    )
    for skill in race_fields["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            defaults={"bonus": skill["bonus"], "race": race}
        )
    return race


if __name__ == "__main__":
    main()
