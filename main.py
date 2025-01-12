import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
        for player_name, value in players.items():
            race, created = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
            for skill_ in value["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_["name"],
                    bonus=skill_["bonus"],
                    race=race,
                )
            if value["guild"]:
                guild, created = Guild.objects.get_or_create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"],
                )
            else:
                guild = None
            Player.objects.create(
                nickname=player_name,
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
