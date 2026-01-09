import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, person_data in data.items():
        race_data = person_data.get("race")
        if race_data is not None:
            race, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={
                    "description": race_data.get("description")
                }
            )
        else:
            continue

        guild_data = person_data.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )
        else:
            guild = None

        skills = race_data.get("skills") or []
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race,
                defaults={
                    "bonus": skill.get("bonus")
                }

            )
        if nickname is not None:
            player, created = Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": person_data.get("email"),
                    "bio": person_data.get("bio"),
                    "race": race,
                    "guild": guild
                }

            )
        else:
            continue


if __name__ == "__main__":
    main()
