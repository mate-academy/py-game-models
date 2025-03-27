import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name in players:
        nickname = name
        email = players[name]["email"]
        bio = players[name]["bio"]

        race = players[name]["race"]
        race_name = race["name"]
        race_description = race["description"]
        race_inst = Race.objects.get_or_create(
            name=race_name, description=race_description
        )

        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race_inst[0]
            )

        guild = players[name].get("guild")
        guild_inst = None
        if guild:
            guild_name = guild["name"]
            guild_description = guild["description"]
            guild_inst = Guild.objects.get_or_create(
                name=guild_name, description=guild_description
            )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_inst[0],
            guild=(guild_inst[0] if guild_inst else None),
        )


if __name__ == "__main__":
    main()
