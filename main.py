import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():

        race_info = info.get("race") or {}
        race_name = race_info.get("name")
        race_description = race_info.get("description")

        if not race_name:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        skills = race_info.get("skills", [])
        for skill in skills:
            skill_name = skill.get("name")
            bonus_name = skill.get("bonus")

            if not skill_name:
                continue

            Skill.objects.get_or_create(
                name=skill_name,
                bonus=bonus_name,
                race=race
            )

        guild_info = info.get("guild") or {}
        guild_name = guild_info.get("name")
        guild_description = guild_info.get("description")

        if guild_name:
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild = None

        email_name = info.get("email")
        bio_name = info.get("bio")

        Player.objects.get_or_create(
            nickname=player,
            email=email_name,
            bio=bio_name,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
