import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    def create_guild(guild: dict) -> None:
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

    def get_guild_id(guild: dict) -> int:
        return Guild.objects.get(name=guild["name"]).id

    def create_race(race: dict) -> None:
        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

    def get_race_id(race: dict) -> int:
        return Race.objects.get(name=race["name"]).id

    def create_skills(race: dict):
        skills = race["skills"]
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=get_race_id(race["name"])
                )





if __name__ == "__main__":
    main()
