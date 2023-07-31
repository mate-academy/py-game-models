import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:

        race = players.get(player).get("race")

        if not Race.objects.filter(name=race.get("name")).exists():
            description = (
                race.get("description") if race.get("description") else None
            )
            Race.objects.create(
                name=race.get("name"),
                description=description
            )

        skills_list = race.get("skills")
        for skill in skills_list:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race_id=Race.objects.get(name=race.get("name")).id
                )

        guild = players.get(player).get("guild")
        if guild is not None:
            if not Guild.objects.filter(name=guild.get("name")).exists():
                description = (
                    guild.get("description")
                    if guild.get("description")
                    else None
                )
                Guild.objects.create(
                    name=guild.get("name"),
                    description=description
                )

        if not Player.objects.filter(nickname=player).exists():
            guild_id = (
                Guild.objects.get(name=guild.get("name")).id
                if guild else None
            )
            race_id = (
                Race.objects.get(name=race.get("name")).id
                if race else None
            )
            Player.objects.create(
                nickname=player,
                email=players.get(player).get("email"),
                bio=players.get(player).get("bio"),
                race_id=race_id,
                guild_id=guild_id
            )


if __name__ == "__main__":
    main()
