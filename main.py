import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, data in players.items():
        player_race = data["race"]
        if not Race.objects.filter(name=player_race["name"]).exists():
            new_race = Race.objects.create(
                name=player_race["name"],
                description=player_race["description"]
            )
        else:
            new_race = Race.objects.get(
                name=player_race["name"],
                description=player_race["description"]
            )

        for player_skill in player_race["skills"]:
            if not Skill.objects.filter(name=player_skill["name"]).exists():
                Skill.objects.create(
                    name=player_skill["name"],
                    bonus=player_skill["bonus"],
                    race=Race.objects.get(name=player_race["name"])
                )
            else:
                Skill.objects.get(
                    name=player_skill["name"], bonus=player_skill["bonus"]
                )

        if data["guild"]:
            player_guild = data["guild"]
            if not Guild.objects.filter(name=player_guild["name"]).exists():
                new_guild = Guild.objects.create(
                    name=player_guild["name"],
                    description=player_guild["description"]
                )
            else:
                new_guild = Guild.objects.get(
                    name=player_guild["name"],
                    description=player_guild["description"]
                )
        else:
            new_guild = None

        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=new_race,
            guild=new_guild
        )


if __name__ == "__main__":
    main()
