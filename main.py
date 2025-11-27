import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():

        race_data = info.get("race", {})
        race_name = race_data.get("name")
        race_description = race_data.get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            name = skill.get("name")
            bonus = skill.get("bonus")

            skill, _ = Skill.objects.get_or_create(
                name=name,
                race=race,
                defaults={"bonus": bonus}
            )

        guild_data = info.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
        else:
            guild = None

        email = info.get("email")
        bio = info.get("bio")
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
