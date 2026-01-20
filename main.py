import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for name, player in data.items():
        guild = player["guild"]
        add_guild = get_or_create_guild(guild) if guild else None
        Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=get_or_create_race(player["race"]),
            guild=add_guild
        )
        print(Player)


def get_or_create_race(race: dict) -> Race:
    try:
        player_race = Race.objects.get(name=race["name"])
    except Race.DoesNotExist:
        player_race = Race.objects.create(
            name=race["name"],
            description=race["description"]
        )

        for current_skill in race["skills"]:
            Skill.objects.create(
                name=current_skill["name"],
                bonus=current_skill["bonus"],
                race=player_race
            )
    return player_race


def get_or_create_guild(guild: dict) -> Guild:
    try:
        player_guild = Guild.objects.get(name=guild["name"])
    except Guild.DoesNotExist:
        player_guild = Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )
    return player_guild


if __name__ == "__main__":
    main()
