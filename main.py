import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
        for player in players:
            race_path = players[player].get("race")

            if players[player].get("guild"):
                guild_path = players[player].get("guild")
                if "description" in guild_path.keys():
                    guild_of_player, _ = Guild.objects.get_or_create(
                        name=guild_path.get("name"),
                        description=guild_path.get("description")
                    )
                else:
                    guild_of_player, _ = Guild.objects.get_or_create(
                        name=guild_path.get("name")
                    )
            else:
                guild_of_player = None

            race_of_player, _ = Race.objects.get_or_create(
                name=race_path.get("name"),
                description=race_path.get("description")
            )

            skills = race_path.get("skills")
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race_of_player
                )

            Player.objects.get_or_create(
                nickname=player,
                email=players[player].get("email"),
                bio=players[player].get("bio"),
                race=race_of_player,
                guild=guild_of_player
            )


if __name__ == "__main__":
    main()
