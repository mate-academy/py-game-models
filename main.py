import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player, player_info in players_data.items():
        race_name = player_info["race"]
        player_guild = player_info.get("guild")

        obj_race, _ = Race.objects.get_or_create(
            name=race_name["name"],
            description=race_name["description"]
        )

        obj_guild = None
        if player_guild:
            obj_guild, _ = Guild.objects.get_or_create(
                name=player_guild["name"],
                description=player_guild.get("description", "")
            )

        for skill in race_name["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=obj_race
            )

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=obj_race,
            guild=obj_guild
        )


if __name__ == "__main__":
    main()
