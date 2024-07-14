import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    for player in data.items():

        race = player[1].get("race", {}).get("name")
        description = player[1].get("race", {}).get("description")
        Race.objects.get_or_create(
            name=race,
            description=description,
        )
        print(Race.objects.all())

        guild_name = player[1].get("guild", {}).get("name", {})
        guild_description = player[1].get("guild", {}).get("description", {})
        Guild.objects.create(
            name=guild_name,
            description=guild_description,
        )

        print(Guild.objects.all())

        skills = player[1].get("race", {}).get("skills")
        for skill in skills:

            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=1,
            )
        print(Skill.objects.all())

        player_name = player[0]
        Player.objects.create(
            nickname=player_name,
            email=player[1].get("email"),
            bio=player[1].get("bio"),
            race_id=1,
            guild_id=1,
        )

        print(Player.objects.all())


if __name__ == "__main__":
    main()
