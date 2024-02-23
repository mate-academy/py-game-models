import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    races = {}
    guilds = {}
    skills = {}

    for player_name, player_data in players_data.items():
        # Race
        race_data = player_data["race"]
        race_name = race_data["name"]
        race_description = race_data["description"]
        if race_name not in races:
            races[race_name] = Race.objects.get_or_create\
                (name=race_name,
                 description=race_description)[0]

        # Guild
        guild_data = player_data.get("guild")
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            if guild_name not in guilds:
                guilds[guild_name] = Guild.objects.get_or_create\
                    (name=guild_name,
                     description=guild_description)[0]

        # Skills
        for skill_data in race_data["skills"]:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            if skill_name not in skills:
                skills[skill_name] = Skill.objects.get_or_create\
                    (name=skill_name,
                     bonus=skill_bonus,
                     race=races[race_name])[0]

    # Create players
    for player_name, player_data in players_data.items():
        race_name = player_data["race"]["name"]
        race = races[race_name]
        guild_data = player_data.get("guild")
        guild = guilds[guild_data["name"]] if guild_data else None
        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
