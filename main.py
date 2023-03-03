import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        file_json = json.load(f)
        for key, value in file_json.items():

            race_exists = Race.objects.filter(
                name=value["race"]["name"]
            ).exists()
            race = (
                Race.objects.get(name=value["race"]["name"])
            ) if race_exists else (Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            ))

            for skill in value["race"]["skills"]:
                skill_exists = Skill.objects.filter(
                    name=skill["name"]
                ).exists()
                if not skill_exists:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )
            if value["guild"]:
                guild_exists = Guild.objects.filter(
                    name=value["guild"]["name"]
                ).exists()
                guild = (
                    Guild.objects.get(
                        name=value["guild"]["name"])
                ) if guild_exists else Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )
            else:
                guild = None

            Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
