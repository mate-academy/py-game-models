import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        file_json = json.load(f)
    for name, player_info in file_json.items():

        race_exists = Race.objects.filter(
            name=player_info["race"]["name"]
        ).exists()
        race = (
            Race.objects.get(name=player_info["race"]["name"])
        ) if race_exists else (Race.objects.create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        ))

        for skill in player_info["race"]["skills"]:
            skill_exists = Skill.objects.filter(
                name=skill["name"]
            ).exists()
            if not skill_exists:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        guild = None
        if player_info["guild"]:
            guild_exists = Guild.objects.filter(
                name=player_info["guild"]["name"]
            ).exists()
            guild = (
                Guild.objects.get(
                    name=player_info["guild"]["name"])
            ) if guild_exists else Guild.objects.create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )

        Player.objects.create(
            nickname=name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
