import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        user_data = json.load(file)

    for nick_name in user_data.keys():

        race_data = user_data[nick_name]["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        guild_data = user_data[nick_name]["guild"]
        if guild_data:
            description_data = guild_data["description"] \
                if guild_data["description"] else None
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=description_data
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nick_name,
            email=user_data[nick_name]["email"],
            bio=user_data[nick_name]["bio"],
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
