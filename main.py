import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> dict:
    with open("players.json") as f:
        players_data = json.load(f)

    for key, value in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={"description": value["race"]["description"]}
        )
        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill["bonus"]},
            )

        guild_data = value.get("guild")

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        else:
            guild = None

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild,
        )

    return {
        "races": Race.objects.all(),
        "skills": Skill.objects.all(),
        "guilds": Guild.objects.all(),
        "players": Player.objects.all(),
    }


if __name__ == "__main__":
    main()
