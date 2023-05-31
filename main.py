import json

import init_django_orm  # noqa: F401

from db.create_guild_and_race import create_race_and_guild
from db.create_skills import create_skills
from db.create_players import create_players
from db.models import Player, Race, Guild, Skill  # noqa: F401


def main() -> None:
    with open("players.json") as data:
        users_data = json.load(data)

        races, guilds = create_race_and_guild(users_data)
        Race.objects.bulk_create(races)
        Guild.objects.bulk_create(guilds)

        skills = create_skills(users_data)
        Skill.objects.bulk_create(skills)
        create_players(users_data)


if __name__ == "__main__":
    main()
