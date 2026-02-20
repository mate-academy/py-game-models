import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_skill(skill: dict, race: Race) -> None:
    Skill.objects.get_or_create(
        name=skill.get("name"),
        defaults={"bonus": skill.get("bonus"), "race": race},
    )


def create_guild(guild: dict) -> None | Guild:
    if guild is None:
        return None
    return Guild.objects.get_or_create(
        name=guild.get("name"),
        defaults={"description": guild.get("description")},
    )[0]


def create_race(race: dict) -> Race:
    new_race = Race.objects.get_or_create(
        name=race.get("name"),
        defaults={"description": race.get("description")},
    )[0]
    for skill in race.get("skills", []):
        create_skill(skill, new_race)
    return new_race


def create_players(players: dict) -> None:
    for name, player in players.items():
        race = create_race(player.get("race"))
        guild = create_guild(player.get("guild"))
        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player.get("email"),
                "bio": player.get("bio"),
                "race": race,
                "guild": guild,
            },
            created_at=player.get("created_at"),
        )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    create_players(players)


if __name__ == "__main__":
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    main()
