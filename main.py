import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, PlayerModel, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for nickname, person in players.items():
        race_info = person["race"]

        Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        for skill in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race_info["name"])
            )

        guide_info = person["guild"]
        guide = None
        if guide_info:
            guide, created = Guild.objects.get_or_create(
                name=guide_info["name"],
                description=guide_info["description"]
            )

        PlayerModel.objects.create(
            nickname=nickname,
            email=person["email"],
            bio=person["bio"],
            race=Race.objects.get(name=race_info["name"]),
            guide=guide,
        )


if __name__ == "__main__":
    main()
