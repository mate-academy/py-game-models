import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)
    for name, data in players_data.items():
        race = data["race"]
        guild = data["guild"]
        skills = race["skills"]

        exists_race = Race.objects.filter(name=race["name"]).exists()
        race = (
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
            if not exists_race else Race.objects.get(name=race["name"])
        )

        if guild:
            exists_guild = Guild.objects.filter(name=guild["name"]).exists()
            guild = (
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
                if not exists_guild else Guild.objects.get(name=guild["name"])
            )

        for skill in skills:
            exists_skill = Skill.objects.filter(name=skill["name"]).exists()
            if not exists_skill:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        exists_player = Player.objects.filter(nickname=name).exists()
        if not exists_player:
            Player.objects.create(
                nickname=name,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
