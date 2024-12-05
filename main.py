import init_django_orm  # noqa: F401
import json

from db.models import Player, Skill, Guild, Race


def main() -> None:
    with open("players.json", "r") as player_file:
        json_data = json.load(player_file)

    for key, value in json_data.items():
        race_obj = None
        if value["race"]:
            race_obj = Race.objects.get_or_create(**{
                "name": value["race"]["name"],
                "description": value["race"]["description"]
            })[0]

            for skill in value["race"]["skills"]:
                skill.update({"race": race_obj})
                Skill.objects.get_or_create(**skill)

        guild_obj = None
        if value["guild"]:
            guild_obj = Guild.objects.get_or_create(**value["guild"])[0]

        value.update({"nickname": key, "race": race_obj, "guild": guild_obj})
        Player.objects.create(**value)


if __name__ == "__main__":
    main()
