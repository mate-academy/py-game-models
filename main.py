import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def make_race(
        race_data: dict
) -> Race:
    name = race_data["name"]

    if not Race.objects.filter(name=name).exists():
        description = race_data["description"]
        Race.objects.create(
            name=name,
            description=description
        )
    return Race.objects.get(name=name)


def make_skills(
        skills_data: dict,
        race: Race
) -> None:
    for skill in skills_data:
        name = skill["name"]
        if not Skill.objects.filter(name=name).exists():
            bonus = skill["bonus"]
            Skill.objects.create(
                name=name,
                bonus=bonus,
                race=race
            )


def make_guild(guild_data: dict) -> Guild or None:
    if guild_data:
        name = guild_data["name"]

        if not Guild.objects.filter(name=name).exists():
            description = guild_data["description"]
            Guild.objects.create(
                name=name,
                description=description
            )
        return Guild.objects.get(name=name)
    return None


def make_player(
        nickname: str,
        email: str,
        bio: str,
        race: Race,
        guild: Guild
) -> None:
    if not Player.objects.filter(nickname=nickname).exists():
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


def main():
    with open("players.json", "r") as data:
        players = json.load(data)

        for player in players:
            nickname = player
            email = players[player]["email"]
            bio = players[player]["bio"]

            race = make_race(players[player]["race"])
            make_skills(players[player]["race"]["skills"], race)
            guild = make_guild(players[player]["guild"])
            make_player(
                nickname,
                email,
                bio,
                race,
                guild
            )


if __name__ == "__main__":
    main()
