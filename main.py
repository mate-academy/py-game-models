import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data_players = json.load(file)

    for player in data_players:
        info = data_players[player]
        race = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )
        guild = Guild.objects.get_or_create(
            name=info["guild"]["name"],
            description=info["guild"]["description"]
        ) if info["guild"] else None
        skills = info["race"]["skills"]
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race if not isinstance(race, tuple) else race[0],
            guild=guild if not isinstance(guild, tuple) else guild[0]
        )
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race if not isinstance(race, tuple) else race[0]
            )


if __name__ == "__main__":
    main()
