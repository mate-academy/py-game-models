import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for player in data:
        name = player
        email = data[player].get("email")
        bio = data[player].get("bio")

        race_data = data[player].get("race")
        race_name = race_data.get("name")
        race_description = race_data.get("description")

        race_instance, created = Race.objects.get_or_create(
            name=race_name,
            description=race_description,
        )

        race_skills_data = race_data.get("skills", [])
        for skill in race_skills_data:
            race_skills_name = skill.get("name")
            race_skills_bonus = skill.get("bonus")
            Skill.objects.get_or_create(
                name=race_skills_name,
                bonus=race_skills_bonus,
                race=race_instance,
            )

        guild_data = data[player].get("guild")
        if guild_data:
            guild = guild_data.get("name")
            guild_description = guild_data.get("description")

            guild_instance, created = Guild.objects.get_or_create(
                name=guild,
                description=guild_description
            )
        else:
            guild_instance = None

        Player.objects.get_or_create(
            nickname=name,
            email=email,
            bio=bio,
            race=race_instance,
            guild=guild_instance)


if __name__ == "__main__":
    main()
