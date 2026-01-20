import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config:
        players = json.loads(config.read())

    for nickname, params in players.items():
        params_race = params["race"]
        race, _ = Race.objects.get_or_create(
            name=params_race["name"],
            description=params_race["description"],
        )

        for skill in params_race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        guild = None
        params_guild = params["guild"]
        if params_guild:
            guild, _ = Guild.objects.get_or_create(
                name=params_guild["name"],
                description=params_guild["description"],
            )

        Player.objects.create(
            nickname=nickname,
            email=params["email"],
            bio=params["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
