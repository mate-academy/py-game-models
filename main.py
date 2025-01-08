import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source_file:
        source_data = json.load(source_file)

    for nick, player in source_data.items():
        race = player.get("race")
        player_race = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )[0]

        skills = race.get("skills")
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=player_race
            )

        guild = player.get("guild")
        player_guild = Guild.objects.get_or_create(
            name=guild.get("name"),
            description=guild.get("description")
        )[0] if guild else None

        Player.objects.create(
            nickname=nick,
            email=player.get("email"),
            bio=player.get("bio"),
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
