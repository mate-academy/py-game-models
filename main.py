import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race_info: dict):
    current_name = race_info["name"]
    current_description = race_info["description"]

    if not Race.objects.filter(name=current_name).exists():
        Race.objects.create(name=current_name,
                            description=current_description)
    return Race.objects.get(name=current_name)


def create_skills(skill_info: dict, current_race: Race):
    for skill in skill_info:
        current_name = skill["name"]
        current_bonus = skill["bonus"]

        if not Skill.objects.filter(name=current_name).exists():
            Skill.objects.create(name=current_name,
                                 bonus=current_bonus,
                                 race=current_race)


def create_guild(guild_info: dict):
    if guild_info:
        current_name = guild_info["name"]
        current_description = guild_info["description"]

        if not Guild.objects.filter(name=current_name).exists():
            Guild.objects.create(name=current_name,
                                 description=current_description)
        return Guild.objects.get(name=current_name)
    return None


def create_player(nickname: str,
                  email: str,
                  bio: str,
                  race: Race,
                  guild: Guild):
    if not Player.objects.filter(nickname=nickname).exists():
        Player.objects.create(nickname=nickname,
                              email=email, bio=bio,
                              race=race, guild=guild)


def main():
    with open("players.json", "r") as file_read:
        player_data = json.load(file_read)

        for player in player_data:
            nickname = player

            email = player_data[nickname]["email"]
            bio = player_data[nickname]["bio"]

            race = create_race(player_data[nickname]["race"])
            create_skills(player_data[nickname]["race"]["skills"], race)
            guild = create_guild(player_data[nickname]["guild"])

            create_player(nickname=nickname,
                          email=email, bio=bio,
                          race=race, guild=guild)


if __name__ == "__main__":
    main()
