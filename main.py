import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict1 = json.load(file)

    for player_name, info in players_dict1.items():
        race_data = info["race"]
        guild_data = info["guild"]

        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
        else:
            guild = None

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill["bonus"]}
            )

        Player.objects.update_or_create(
            nickname=player_name,
            defaults={"email": info["email"],
                      "bio": info["bio"],
                      "race": race,
                      "guild": guild}
        )


if __name__ == "__main__":
    main()
