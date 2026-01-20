import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as source_file:
        source_data = json.load(source_file)

    for key, value in source_data.items():
        race, race_bool = Race.objects.get_or_create(
            name=value.get("race").get("name"),
            description=value.get("race").get("description")
        )

        skills = value.get("race").get("skills")
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        guild_data = value.get("guild")
        guild = None
        if guild_data:
            guild, guild_bool = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        Player.objects.create(
            nickname=key,
            email=value.get("email"),
            bio=value.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
