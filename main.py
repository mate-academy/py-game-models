import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for player in players:
            email = players.get(player).get("email")
            bio = players.get(player).get("bio")
            race = players.get(player).get("race")
            skills = players.get(player).get("race").get("skills")
            guild = players.get(player).get("guild")

    try:
        current_guild = Guild.objects.get_or_create(
            name=guild.get("name"),
            description=guild.get("description")
        )
    except AttributeError:
        current_guild = None

    current_race = Race.objects.get_or_create(
        name=race.get("name"),
        description=race.get("description")
    )

    try:
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=current_race[0]
            )
    except TypeError:
        pass

    if current_guild:
        Player.objects.get_or_create(
            nickname=player,
            email=email,
            bio=bio,
            race=current_race[0],
            guild=current_guild[0]
        )
    if not current_guild:
        Player.objects.get_or_create(
            nickname=player,
            email=email,
            bio=bio,
            race=current_race[0],
        )


if __name__ == "__main__":
    main()
