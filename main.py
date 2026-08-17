import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        races = json.load(f)
        # print(races)
        for key, race in races.items():
            print(race)
            race_obj, _ = Race.objects.get_or_create(
                name=race["race"]["name"],
                description=race["race"]["description"]
            )

            for skill in race["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

            guild_obj = None
            if race["guild"]:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=race["guild"]["name"],
                    description=race["guild"]["description"]
                )

            Player.objects.get_or_create(
                nickname=key,
                email=race["email"],
                bio=race["bio"],
                race=Race.objects.get(name=race["race"]["name"]),
                guild=guild_obj
            )


if __name__ == "__main__":
    main()
