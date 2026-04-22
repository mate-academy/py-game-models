import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for nickname, datum in data.items():
        race_data = datum.get("race")
        if race_data and isinstance(race_data, dict):
            race_name = race_data.get("name")
            race_desc = race_data.get("description", "")
            if race_name:
                race, _ = Race.objects.get_or_create(
                    name=race_name,
                    description=race_desc
                )
        else:
            race = None

        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)

        guild_data = datum.get("guild")
        guild = None
        if guild_data and isinstance(guild_data, dict):
            guild_name = guild_data.get("name")
            guild_desc = guild_data.get("description", "")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(name=guild_name,
                                                       description=guild_desc)

        Player.objects.create(nickname=nickname,
                              email=datum["email"],
                              bio=datum["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
