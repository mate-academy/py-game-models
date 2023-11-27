import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)
    for nickname, user in data.items():
        race_info = user["race"]
        race, created = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )
        for skill_ in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill_["name"],
                bonus=skill_["bonus"],
                race=race
            )
        guild = None
        if user["guild"]:
            name = user["guild"]["name"]
            description = user["guild"]["description"]
            Guild.objects.get_or_create(
                name=name,
                description=description
            )
            guild = Guild.objects.get(name=user["guild"]["name"])
        Player.objects.get_or_create(
            nickname=nickname,
            email=user["email"],
            bio=user["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
