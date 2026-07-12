import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_value in players.items():
        race_value = player_value["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_value["name"],
            defaults={"description": race_value["description"]}
        )

        for skill in race_value["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race_obj,
                defaults={"bonus": skill["bonus"]}
            )

        guild_value = player_value.get("guild")
        if guild_value:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_value["name"],
                defaults={"description": guild_value["description"]}
            )
        else:
            guild_obj = None

        player_obj, _ = Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": player_value["email"],
                "bio": player_value["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
