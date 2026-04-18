import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player in data:
        race_name = data[player]["race"]["name"]
        race_description = data[player]["race"]["description"]
        race, created = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        guild_name = data[player]["guild"]
        guild = None
        if guild_name:
            guild, created = Guild.objects.get_or_create(
                name=guild_name.get("name"),
                description=guild_name.get("description")
            )
        for skill in data[player]["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)

        Player.objects.get_or_create(nickname=player,
                                     email=data[player]["email"],
                                     bio=data[player]["bio"],
                                     race=race,
                                     guild=guild)


if __name__ == "__main__":
    main()
