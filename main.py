import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for person in data:
        race, _ = Race.objects.get_or_create(name=data[person]["race"]["name"],
                                             description=data[person]["race"]["description"])
        for skill in data[person]["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)
        guild_data = data["guild"]
        if guild_data is not None:
            guild_name = data["guild"]["name"]
            guild_description = data["guild"]["description"]
            guild_info = Guild.objects.get_or_create(
                name=guild_name, description=guild_description)
        else:
            guild_info = None

        player, _ = Player.objects.get_or_create(name=person,
                                                 email=data[person]["email"],
                                                 bio=data[person]["bio"],
                                                 race=race,
                                                 guild=guild_info)


if __name__ == "__main__":
    main()
