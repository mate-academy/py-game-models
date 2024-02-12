import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for nickname, player_data in players.items():
        race, race_created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
        if race_created and "skills" in player_data["race"]:
            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        player_guild = player_data.get("guild")
        if player_guild:
            guild, created = Guild.objects.get_or_create(**player_guild)
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
