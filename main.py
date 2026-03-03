import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        race = player_data.get("race")
        guild = player_data.get("guild")

        if race:
            skills = race.get("skills")
            race_model = create_race(race)
            if skills:
                create_skills(skills, race_model)
        else:
            race_model = None

        guild_model = create_guild(guild)

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race_model,
            guild=guild_model,
        )


def create_race(race: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race.get("name"),
        defaults={"description": race.get("description")}
    )
    return race


def create_guild(guild: dict | None) -> Guild | None:
    if guild:
        guild, _ = Guild.objects.get_or_create(
            name=guild.get("name"),
            defaults={"description": guild.get("description")}
        )
        return guild
    return None


def create_skills(skills: list, race: Race) -> None:
    for skill in skills:
        Skill.objects.get_or_create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race,
        )


if __name__ == "__main__":
    main()
