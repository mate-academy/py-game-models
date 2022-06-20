import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


FILE_NAME = "players.json"


def parse_file():
    with open(FILE_NAME) as f:
        players_data = json.load(f)
    return players_data


def create_race(race_name: str, race_description: str):
    if not Race.objects.filter(name=race_name).exists():
        if race_description:
            Race.objects.create(
                name=race_name,
                description=race_description
            )
        else:
            Race.objects.create(name=race_name)


def create_skills(skills: dict, race):
    if skills:
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


def create_guild(guild_name: str, guild_description: str):
    if not Guild.objects.filter(name=guild_name).exists():
        if guild_description:
            Guild.objects.create(
                name=guild_name,
                description=guild_description
            )
        else:
            Guild.objects.create(name=guild_name)


def create_player(
        nickname: str,
        email: str,
        bio: str,
        race,
        guild
):
    if Guild:
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )
    else:
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race
        )


def main():
    players_data = parse_file()

    for nickname, data in players_data.items():

        race_name = data["race"]["name"]
        race_description = data["race"]["description"]
        create_race(race_name, race_description)

        race = Race.objects.get(name=race_name)
        skills = data["race"]["skills"]
        create_skills(skills, race)

        guild = None
        if data["guild"]:
            guild_name = data["guild"]["name"]
            guild_description = data["guild"]["description"]
            create_guild(guild_name, guild_description)
            guild = Guild.objects.get(name=guild_name)

        email = data["email"]
        bio = data["bio"]

        create_player(nickname, email, bio, race, guild)

    print("done")


if __name__ == "__main__":
    main()
