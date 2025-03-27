import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def create_skill(name: str, bonus: str, race: Race) -> Skill:
    return Skill.objects.create(
        name=name, bonus=bonus, race=race
    )


def create_race(name: str, description: str, skills: list) -> Race:
    if not Race.objects.filter(name=name).exists():
        race_value = Race.objects.create(
            name=name,
            description=description
        )
        for skill in skills:
            create_skill(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_value
            )
    else:
        race_value = Race.objects.get(name=name)
    return race_value


def create_guild(name: str, description: str) -> Guild:
    guild_value = None
    if not Guild.objects.filter(name=name).exists():
        guild_value = Guild.objects.create(
            name=name,
            description=description
        )
    elif Guild.objects.filter(name=name).exists():
        guild_value = Guild.objects.get(name=name)
    return guild_value


def main() -> None:
    with open("players.json", "r") as data:
        players = json.load(data)

    for name, attribute in players.items():
        race_value = create_race(
            attribute.get("race", {}).get("name"),
            attribute.get("race", {}).get("description"),
            attribute.get("race", {}).get("skills")
        )

        guild_value = None

        if attribute.get("guild"):
            guild_value = create_guild(
                name=attribute.get("guild", {}).get("name"),
                description=attribute.get("guild", {}).get("description")
            )

        Player.objects.create(
            nickname=name,
            email=attribute["email"],
            bio=attribute["bio"],
            race=race_value,
            guild=guild_value,
        )


if __name__ == "__main__":
    main()
