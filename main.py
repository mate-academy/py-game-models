import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    race_inst = None
    guild_inst = None

    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player in players.items():
        if not Race.objects.filter(name=player["race"]["name"]).exists():
            race_inst = Race.objects.create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            )

        for skill in player["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_inst
                )

        guild = player.get("guild")
        if guild is not None:
            if not Guild.objects.filter(name=player["guild"]["name"]).exists():
                guild_inst = Guild.objects.create(
                    name=player["guild"]["name"],
                    description=(
                        player["guild"]["description"]
                        if player["guild"]["description"] else None
                    )
                )
        else:
            guild_inst = None

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=race_inst,
                guild=guild_inst
            )


if __name__ == "__main__":
    main()
