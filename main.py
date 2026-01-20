import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for name, player_stats in players.items():
        if Race.objects.filter(name=player_stats["race"]["name"]).exists():
            race = Race.objects.get(name=player_stats["race"]["name"])
        else:
            race = Race.objects.create(
                name=player_stats["race"]["name"],
                description=player_stats["race"]["description"],
            )

        for skill in player_stats["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=race
                )

        if player_stats["guild"]:
            if Guild.objects.filter(
                    name=player_stats["guild"]["name"]
            ).exists():
                guild = Guild.objects.get(name=player_stats["guild"]["name"])
            else:
                guild = Guild.objects.create(
                    name=player_stats["guild"]["name"],
                    description=player_stats["guild"]["description"],
                )
        else:
            guild = None
        Player.objects.create(
            nickname=name,
            email=player_stats["email"],
            bio=player_stats["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
