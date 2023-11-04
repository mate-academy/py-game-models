import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

with open("players.json", "r") as file:
    data = json.load(file)


def main() -> None:
    for nickname, data_player in data.items():
        race_data = data_player["race"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        guild = None
        if data_player["guild"] is not None:
            guild_data = data_player["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data_player["email"],
                "bio": data_player["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
