import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()
    with open("players.json", "r") as players_json:
        players = json.load(players_json)
        for nickname, bio in players.items():
            guild = get_or_create_guild(bio)
            race = get_or_create_race(bio)
            create_skills(bio, race)
            create_player(nickname=nickname, race=race, guild=guild, bio=bio)


def create_skills(bio: dict, race: Race) -> None:
    skills_list = bio.get("race").get("skills")
    # print(skills_list)
    # print(race)
    for skill in skills_list:
        try:
            Skill.objects.get_or_create(
                race=race,
                name=skill.get("name"),
                bonus=skill.get("bonus"),
            )
        except Exception as e:
            print(e)
    return None


def get_or_create_guild(bio: dict) -> Guild | None:
    if guild_bio := bio.get("guild"):
        try:
            guild, _ = Guild.objects.get_or_create(
                name=guild_bio.get("name"),
                description=guild_bio.get("description"),
            )
            return guild
        except Exception as e:
            print(e)
    return None


def get_or_create_race(bio: dict) -> Guild | None:
    if guild_bio := bio.get("race"):
        try:
            race, _ = Race.objects.get_or_create(
                name=guild_bio.get("name"),
                description=guild_bio.get("description"),
            )
            return race
        except Exception as e:
            print(e)
    return None


def create_player(
        nickname: str,
        bio: dict,
        race: Race,
        guild: Guild
) -> None:
    player = Player(
        nickname=nickname,
        email=bio.get("email"),
        bio=bio.get("bio"),
        race=race,
        guild=guild
    )
    player.save()


if __name__ == "__main__":
    main()
