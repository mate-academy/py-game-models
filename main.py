import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

        for nickname, player_data in data.items():
            race, is_created = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )
            for skill_data in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                )
            guild = None
            if player_data["guild"]:
                guild, is_created = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"]
                )

            Player.objects.create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()