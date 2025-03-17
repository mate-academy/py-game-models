import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, player in players.items():
        race = player.get('race')
        if race:
            player_race = Race.objects.get_or_create(
                name=race.get('name'),
                description=race.get('description')
            )

            for skill in race.get('skills'):
                Skill.objects.get_or_create(
                    name=skill.get('name'),
                    bonus=skill.get('bonus'),
                    race=player_race[0]
                )
        else:
            player_race = None

        guild = player.get("guild")
        if guild:
            player_guild = Guild.objects.get_or_create(
                name=guild.get('name'),
                description=guild.get('description')
            )
        else:
            player_guild = [None]

        Player.objects.get_or_create(
            nickname=name,
            email=player.get('email'),
            bio=player.get('bio'),
            race=player_race[0],
            guild=player_guild[0]
        )


if __name__ == "__main__":
    main()
