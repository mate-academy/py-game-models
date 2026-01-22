import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    for name, player_info in players_info.items():

        players_race = player_info["race"]
        if players_race:
            players_race, if_exists = Race.objects.get_or_create(
                name=players_race["name"],
                description=players_race["description"]
            )

        for player_skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=player_skill["name"],
                bonus=player_skill["bonus"],
                race=players_race
            )

        players_guild = player_info["guild"]
        if players_guild:
            players_guild, if_exists = Guild.objects.get_or_create(
                name=players_guild["name"],
                description=players_guild["description"]
            )

        Player.objects.get_or_create(
            nickname=name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=players_race,
            guild=players_guild
        )


if __name__ == "__main__":
    main()
