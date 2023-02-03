import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)
    player_race = None
    player_guild = None

    for person_name, info in players_data.items():
        if not Race.objects.filter(
            name=info["race"]["name"], description=info["race"]["description"]
        ).exists():
            player_race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        if info["guild"]:
            if Guild.objects.filter(
                    name=info["guild"]["name"]).exists() is False:
                player_guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=player_race
                )
        Player.objects.create(
            nickname=person_name,
            email=info["email"],
            bio=info["bio"],
            race=player_race,
            guild=player_guild if info["guild"] else None,
        )


if __name__ == "__main__":
    main()
