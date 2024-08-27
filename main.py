import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player, info in players.items():
        race = info["race"]
        guild = info["guild"]

        new_race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )[0]

        if guild:
            new_guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )[0]
        else:
            new_guild = guild

        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race,
            )

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=new_race,
            guild=new_guild
        )


if __name__ == "__main__":
    main()
