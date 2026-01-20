import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, data_player in data.items():
        race_data = data_player.get("race")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")}
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"bonus": skill.get("bonus"), "race": race}
            )

        guild = None
        if data_player["guild"] is not None:
            guild_data = data_player.get("guild")
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data_player.get("email"),
                "bio": data_player.get("bio"),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
