import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as info:
        info_players = json.load(info)

    race = None
    guild = None
    for name, info_player in info_players.items():
        if not Race.objects.filter(
                name=info_player["race"]["name"]
        ).exists():
            race = Race.objects.create(
                name=info_player["race"]["name"],
                description=info_player["race"]["description"]
            )
            for info_skills in info_player["race"]["skills"]:
                Skill.objects.create(
                    name=info_skills["name"],
                    bonus=info_skills["bonus"],
                    race=race
                )
        if info_player["guild"]:
            if not Guild.objects.filter(
                    name=info_player["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=info_player["guild"]["name"],
                    description=info_player["guild"]["description"]
                )
        else:
            guild = None

        Player.objects.create(
            nickname=name,
            email=info_player["email"],
            bio=info_player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
