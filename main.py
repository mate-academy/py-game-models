import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    content = {}
    with open("players.json", "r") as file:
        string = file.read()
        content = json.loads(string)
    for key in content:
        race, _ = Race.objects.get_or_create(
            name=content[key]["race"]["name"],
            description=content[key]["race"]["description"])
        for skill in content[key]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race)
        guild = None
        if content[key].get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=content[key]["guild"]["name"],
                description=content[key]["guild"]["description"])
        Player.objects.get_or_create(
            nickname=key,
            email=content[key]["email"],
            bio=content[key].get("bio"),
            race=race,
            guild=guild)


if __name__ == "__main__":
    main()
