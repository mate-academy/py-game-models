import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, data in players.items():
        race_data = data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")}
        )

        for skill_data in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                race=race,
                name=skill_data.get("name"),
                defaults={"bonus": skill_data.get("bonus")}
            )

        guild = None
        guild_data = data.get("guild")
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={"email": data.get("email"),
                      "bio": data.get("bio"),
                      "race": race,
                      "guild": guild},
        )


if __name__ == "__main__":
    main()
