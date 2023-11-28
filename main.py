import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        json_data = json.load(file)
    for name in json_data:
        race, _ = Race.objects.get_or_create(
            name=json_data[name]["race"]["name"],
            description=json_data[name]["race"]["description"]
        )
        for skill in json_data[name]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        if json_data[name]["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=json_data[name]["guild"]["name"],
                description=json_data[name]["guild"]["description"]
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=name,
            email=json_data[name]["email"],
            bio=json_data[name]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
