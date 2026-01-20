import json

import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for person in data:
        player = data.get(person)
        race = player.get("race")
        skills = race.get("skills")
        guild = player.get("guild")

        race = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        if guild:
            guild = Guild.objects.get_or_create(**guild)[0]

        Player.objects.create(
            nickname=person,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
