import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_skills(skills: list, race: Race) -> None:
    for skill in skills:
        if not Skill.objects.filter(name=skill.get("name")).exists():
            race.skill_set.create(
                name=skill.get("name"), bonus=skill.get("bonus")
            )


def create_race(race_data: dict) -> Race:
    player_race, _ = Race.objects.get_or_create(
        name=race_data.get("name"),
        description=race_data.get("description"),
    )
    return player_race


def create_guild(guild_data: dict) -> Guild:
    if guild_data:
        guild_data, _ = Guild.objects.get_or_create(
            name=guild_data.get("name"),
            description=guild_data.get("description"),
        )
    return guild_data


def create_player(
    name: str, email: str, bio: str, race: Race, guild: Guild
) -> None:
    Player.objects.create(
        nickname=name,
        email=email,
        bio=bio,
        race=race,
        guild=guild,
    )


def main() -> None:
    with open("players.json", "r") as file:
        data = json.loads(file.read())
    for nick, info in data.items():
        race_data = info.get("race")
        guild_data = info.get("guild")
        skills = info.get("race").get("skills")
        player_race = create_race(race_data)
        player_guild = create_guild(guild_data)
        if skills:
            create_skills(skills, player_race)
        create_player(
            nick, info.get("email"), info.get("bio"), player_race, player_guild
        )


if __name__ == "__main__":
    main()
