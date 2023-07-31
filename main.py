import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        data = json.load(json_file)

    for name, user_data in data.items():
        current_race = user_data["race"]
        if Race.objects.filter(name=current_race["name"]).exists():
            race = Race.objects.filter(name=current_race["name"]).get()
        else:
            race = Race.objects.create(
                name=current_race["name"],
                description=current_race["description"]
            )

        current_guild = user_data["guild"]
        if current_guild:
            if Guild.objects.filter(name=current_guild["name"]).exists():
                guild = Guild.objects.filter(name=current_guild["name"]).get()
            else:
                guild = Guild.objects.create(
                    name=current_guild["name"],
                    description=current_guild["description"]
                )
        else:
            guild = None

        current_list_of_skills = user_data["race"]["skills"]

        for skill in current_list_of_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild_id = guild.id if guild else None

        Player.objects.create(
            nickname=name,
            email=user_data["email"],
            bio=user_data["bio"],
            race_id=race.id,
            guild_id=guild_id,
        )


if __name__ == "__main__":
    main()
