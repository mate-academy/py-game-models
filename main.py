import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        user_data = json.load(file)

    for nick_name, data in user_data.items():

        race_data = data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        guild_data = data["guild"]
        if guild_data:
            description_data = guild_data["description"] \
                if guild_data["description"] else None
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=description_data
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nick_name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
