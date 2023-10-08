import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        guild = player_info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )

        race = player_info.get("race")
        if race:
            race, _ = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        skills = player_info["race"]["skills"]
        if skills:
            for skill in skills:
                skill_obj, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
