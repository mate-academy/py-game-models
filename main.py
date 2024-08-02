import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for user, user_data in data.items():
        race_name = user_data["race"]["name"]
        race_description = user_data["race"]["description"]
        race, created_race = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        for skill in user_data["race"]["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )
        guild = None
        if user_data["guild"]:
            guild_data = user_data.get("guild", {})
            guild_name = guild_data.get("name", None)
            guild_description = guild_data.get("description", None)
            guild, create = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        Player.objects.create(
            nickname=user,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
