import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for name, data in players.items():

        race, create = Race.objects.get_or_create(
            name=data.get("race").get("name"),
            description=data.get("race").get("description")
        )

        for skill in data.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        guild = data.get("guild")
        if guild:
            guild, create = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        Player.objects.get_or_create(
            nickname=name,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
